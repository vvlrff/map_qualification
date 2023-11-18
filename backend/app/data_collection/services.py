import os
import requests
import pandas as pd
import numpy as np
import spacy
import pickle
from transformers import MarianMTModel, MarianTokenizer
import geonamescache
import logging
from app.data_collection.scrapper import get_guardian_news_items

# Настройка логгирования
logging.basicConfig(filename='news_processing.log', level=logging.DEBUG)

nlp = spacy.load('en_core_web_lg')
gc = geonamescache.GeonamesCache()

current_directory = os.path.dirname(os.path.abspath(__file__))
model_pickle_path = os.path.join(current_directory, 'model_pickle')

model_name_translator = "Helsinki-NLP/opus-mt-en-ru"
model_translator = MarianMTModel.from_pretrained(model_name_translator)
tokenizer_translator = MarianTokenizer.from_pretrained(model_name_translator)

# Настройка логгера
logger = logging.getLogger(__name__)


def preprocess_text(text):
    doc = nlp(text)
    return ' '.join(token.lemma_ for token in doc if not token.is_stop and not token.is_space and not token.is_punct)


def dangerous_news_guardian():
    df = pd.DataFrame(get_guardian_news_items())
    df['preprocessing_text'] = df['title'].apply(preprocess_text)
    df['vector'] = df['preprocessing_text'].apply(
        lambda text: nlp(text).vector)
    preprocessing_text = np.stack(df['vector'])

    with open(model_pickle_path, 'rb') as file:
        rfc = pickle.load(file)

    y_pred = rfc.predict(preprocessing_text)

    relevant_items = df[y_pred == 1]
    need_list = relevant_items['title'].tolist()
    image_list = relevant_items['image'].tolist()
    url_list = relevant_items['href'].tolist()

    all_news_data = []

    for title, image, href in zip(need_list, image_list, url_list):
        text_to_translate = title
        inputs = tokenizer_translator.encode(
            text_to_translate, return_tensors="pt")
        translated = model_translator.generate(inputs)
        translation = tokenizer_translator.decode(
            translated[0], skip_special_tokens=True)

        file_name = os.path.basename(image.split("?")[0])
        save_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', 'photos', file_name))

        response = requests.get(image)

        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            logger.info(f"Изображение {file_name} успешно загружено")
        else:
            logger.error(f"Ошибка при загрузке изображения {file_name}")

        new_string = save_path.split("\\")

        news_data = {
            "title_en": title,
            "title_ru": translation,
            "id": len(all_news_data),
            "href": href,
            "image": new_string[-1],
        }

        found_countries = []
        found_cities = []

        for ent in nlp(title).ents:
            if ent.label_ == 'GPE':
                country_city_name = ent.text
                if country_city_name in gc.get_countries_by_names():
                    found_countries.append(country_city_name)
                elif country_city_name not in gc.get_cities():
                    if country_city_name == "US":
                        found_countries.append("United States of America")
                    elif country_city_name == "UK":
                        found_countries.append("United Kingdom")
                    else:
                        found_countries.append(country_city_name)
                if country_city_name in gc.get_cities():
                    found_cities.append(country_city_name)

        news_data["country"] = found_countries
        news_data["city"] = found_cities
        news_data["topical_keywords"] = None
        all_news_data.append(news_data)
        logger.info(f"Новость {news_data['id']}: {news_data} успешно создана")

    return all_news_data
