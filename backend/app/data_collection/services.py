import os
import requests
import pandas as pd
import spacy
import torch
from transformers import MarianMTModel, MarianTokenizer, AlbertTokenizer, AlbertForSequenceClassification
import geonamescache
import logging
from app.data_collection.scrapper import get_guardian_news_items


nlp = spacy.load('en_core_web_md')
gc = geonamescache.GeonamesCache()

current_directory = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_directory, 'albert_model')

loaded_model = AlbertForSequenceClassification.from_pretrained(model_path)
tokenizer = AlbertTokenizer.from_pretrained(model_path)

model_name_translator = "Helsinki-NLP/opus-mt-en-ru"
model_translator = MarianMTModel.from_pretrained(model_name_translator)
tokenizer_translator = MarianTokenizer.from_pretrained(model_name_translator)


def dangerous_news_guardian():
    df = pd.DataFrame(get_guardian_news_items())

    df['predicted_class'] = None

    # Пройдите по каждой строке в столбце "title"
    for index, row in df.iterrows():
        text_to_classify = [row['title']] 

        # Токенизация и предсказание класса
        inputs = tokenizer(text_to_classify, return_tensors="pt")
        outputs = loaded_model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()

        # Сохранение предсказанного класса в новую колонку
        df.at[index, 'predicted_class'] = predicted_class


    relevant_items = df['predicted_class' == 1]
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
        else:
            logging.error(f"Ошибка при загрузке изображения {file_name}")

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
                if country_city_name in gc.get_cities():
                    found_cities.append(country_city_name)
                elif country_city_name not in gc.get_cities() and country_city_name not in gc.get_countries_by_names():
                    if country_city_name == "US":
                        found_countries.append("United States of America")
                    elif country_city_name == "UK":
                        found_countries.append("United Kingdom")
                    else:
                        found_cities.append(country_city_name)
                if country_city_name in gc.get_countries_by_names():
                        found_countries.append(country_city_name)

        news_data["country"] = found_countries
        news_data["city"] = found_cities
        news_data["topical_keywords"] = None
        all_news_data.append(news_data)
        logging.info(f"Новость {news_data['id']}: {news_data} успешно создана")

    return all_news_data
