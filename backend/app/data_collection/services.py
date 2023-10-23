import requests
from app.data_collection.scrapper import get_news_theguardian
from transformers import MarianMTModel, MarianTokenizer, BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import pandas as pd
import spacy
import numpy as np
import pickle
import os
import geonamescache

nlp = spacy.load('en_core_web_lg')
gc = geonamescache.GeonamesCache()

current_directory = os.path.dirname(os.path.abspath(__file__))
model_pickle_path = os.path.join(current_directory, 'model_pickle')

model_name_translator = "Helsinki-NLP/opus-mt-en-ru"
model_translator = MarianMTModel.from_pretrained(model_name_translator)
tokenizer_translator = MarianTokenizer.from_pretrained(model_name_translator)

model_name_img_text = "Salesforce/blip-image-captioning-large"
model_img_text = BlipForConditionalGeneration.from_pretrained(model_name_img_text)
processor_img_text = BlipProcessor.from_pretrained(model_name_img_text)


def dangerous_news_guardian():
    df = pd.DataFrame(get_news_theguardian())
    preprocessing_text = []

    for text in df['title']:
        doc = nlp(text)
        new_text = [token.lemma_ for token in doc if not token.is_stop and not token.is_space and not token.is_punct]
        preprocessing_text.append(' '.join(new_text))

    df['preprocessing_text'] = preprocessing_text
    df['vector'] = df['preprocessing_text'].apply(lambda text: nlp(text).vector)
    preprocessing_text = np.stack(df.vector)

    with open(model_pickle_path, 'rb') as file:
        rfc = pickle.load(file)

    y_pred = rfc.predict(preprocessing_text)

    need_list = df[y_pred == 1]['title'].tolist()
    image_list = df[y_pred == 1]['image'].tolist()
    url_list = df[y_pred == 1]['href'].tolist()

    items = []

    for title, image, href in zip(need_list, image_list, url_list):
        items.append({
            "title": title,
            "id": len(items),
            "href": href,
            "image": image
        })

    countries = gc.get_countries_by_names()
    cities = gc.get_cities()

    def extract_names(var, key):
        if isinstance(var, dict):
            if key in var:
                yield var[key]
            for k, v in var.items():
                if isinstance(v, (dict, list)):
                    yield from extract_names(v, key)
        elif isinstance(var, list):
            for d in var:
                yield from extract_names(d, key)

    countries = list(extract_names(countries, 'name'))
    cities = list(extract_names(cities, 'name'))

    items = []

    for title, image, href in zip(need_list, image_list, url_list):
        text_to_translate = title
        inputs = tokenizer_translator.encode(text_to_translate, return_tensors="pt")
        translated = model_translator.generate(inputs)
        translation = tokenizer_translator.decode(translated[0], skip_special_tokens=True)

        file_name = os.path.basename(image.split("?")[0]) 
        save_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'photos', file_name))

        response = requests.get(image)

        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Изображение {file_name} успешно загружено")
        else:
            print(f"Ошибка {file_name}")

        image_path = save_path 

        image_ = Image.open(image_path)
        image_bytes = processor_img_text(images=image_, return_tensors="pt").pixel_values
        caption = model_img_text.generate(image_bytes)
        caption_text = processor_img_text.decode(caption[0], skip_special_tokens=True)

        text_to_translate_img = caption_text
        inputs_img = tokenizer_translator.encode(text_to_translate_img, return_tensors="pt")
        translated_img = model_translator.generate(inputs_img)
        translation_img = tokenizer_translator.decode(translated_img[0], skip_special_tokens=True)

        new_string = save_path.split("\\")

        item = {
            "title_en": title,
            "title_ru": translation,
            "id": len(items),
            "href": href,
            "image": new_string[-1],
            "image_text_en": caption_text,
            "image_text_ru": translation_img,
        }

        doc = nlp(title)
        found_countries = []
        found_cities = []
        for ent in doc.ents:
            if ent.label_ == 'GPE':
                country_city_name = ent.text
                if country_city_name in countries:
                    found_countries.append(country_city_name)
                elif country_city_name not in cities:
                    if country_city_name == "US":
                        found_countries.append("United States of America")
                    elif country_city_name == "UK":
                        found_countries.append("United Kingdom")
                    else:
                        found_countries.append(country_city_name)
                if country_city_name in cities:
                    found_cities.append(country_city_name)

        item["country"] = found_countries
        item["city"] = found_cities
        items.append(item)
        print(f"item{id}: {item}")
    
    return items