import app.data_collection.scrapper as _scrapper
import pandas as pd
import spacy
import numpy as np
import pickle
import geonamescache

nlp = spacy.load('en_core_web_lg')
gc = geonamescache.GeonamesCache()


def dangerous_news_guardian():
    df = pd.DataFrame(_scrapper.get_news_theguardian())
    preprocessing_text = []

    for text in df['title']:
        doc = nlp(text)
        new_text = []
        for token in doc:
            if not token.is_stop and not token.is_space and not token.is_punct:
                new_text.append(token.lemma_)
        preprocessing_text.append(' '.join(new_text))

    df['preprocessing_text'] = preprocessing_text
    df['vector'] = df['preprocessing_text'].apply(
        lambda text: nlp(text).vector)

    preprocessing_text = np.stack(df.vector)

    with open('app/data_collection/model_pickle', 'rb') as file:
        rfc = pickle.load(file)
    y_pred = rfc.predict(preprocessing_text)

    need_list = []
    url_list = []

    i = 0
    for item in df['title']:
        if y_pred[i] == 1:
            print(item, y_pred[i])
            need_list.append(item)
        i += 1

    i = 0
    for it in df['href']:
        if y_pred[i] == 1:
            print(item, y_pred[i])
            url_list.append(it)
        i += 1

    items = []
    for i in range(len(need_list)):
        items.append(
            {
                "title": need_list[i],
                "href": url_list[i]
            }
        )

    return items

    


def get_guardian_news_countries():
    df = pd.DataFrame(_scrapper.get_news_theguardian())
    preprocessing_text = []

    for text in df['title']:
        doc = nlp(text)
        new_text = []
        for token in doc:
            if not token.is_stop and not token.is_space and not token.is_punct:
                new_text.append(token.lemma_)
        preprocessing_text.append(' '.join(new_text))

    df['preprocessing_text'] = preprocessing_text
    df['vector'] = df['preprocessing_text'].apply(
        lambda text: nlp(text).vector)

    preprocessing_text = np.stack(df.vector)

    with open('app/data_collection/model_pickle', 'rb') as file:
        rfc = pickle.load(file)

    y_pred = rfc.predict(preprocessing_text)

    need_list = []
    url_list = []
    i = 0

    for item in df['title']:
        if y_pred[i] == 1:
            print(item, y_pred[i])
            need_list.append(item)
        i += 1

    i = 0

    for it in df['href']:
        if y_pred[i] == 1:
            print(item, y_pred[i])
            url_list.append(it)
        i += 1

    items = []
    for i in range(len(need_list)):
        items.append(
            {
                "title": need_list[i],
                "id": i,
                "href": url_list[i]
            }
        )

    countries = gc.get_countries()
    cities = gc.get_cities()

    def gen_dict_extract(var, key):
        if isinstance(var, dict):
            for k, v in var.items():
                if k == key:
                    yield v
                if isinstance(v, (dict, list)):
                    yield from gen_dict_extract(v, key)
        elif isinstance(var, list):
            for d in var:
                yield from gen_dict_extract(d, key)

    countries = [*gen_dict_extract(countries, 'name')]

    cities = [*gen_dict_extract(cities, 'name')]

    info = []
    for item in range(len(need_list)):
        doc = nlp(need_list[item])
        for ent in doc.ents:
            if ent.label_ == 'GPE':
                if ent.text in countries:
                    info.append(
                        {
                            "country": ent.text,
                            "text": doc.text
                        }
                    )
                elif ent.text not in cities:

                    if ent.text == "US":
                        info.append(
                        {
                            "country": "United States of America",
                            "text": doc.text
                        }
                    )
                    elif ent.text == "UK":
                        info.append(
                        {
                            "country": "United Kingdom",
                            "text": doc.text
                        }
                    )
                    else:
                        info.append(
                            {
                                "country": ent.text,
                                "text": doc.text
                            }
                        )
    return info
