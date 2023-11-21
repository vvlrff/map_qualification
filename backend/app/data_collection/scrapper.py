from bs4 import BeautifulSoup
import requests
import logging


def get_guardian_news_items():
    url = 'https://www.theguardian.com/world'
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.799 Yowser/2.5 Safari/537.36'
    }

    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')

    items = []

    for href, text, image in zip(
        soup.find_all(class_="dcr-lv2v9o"),
        soup.find_all(class_="show-underline dcr-1r9ptb2"),
        soup.find_all(class_="dcr-evn1e9")
    ):
        try:
            item_text = text.text
            item_href = href.get('href')
            item_image = image.get('src')

            full_href = f"https://www.theguardian.com{item_href}"
            items.append({
                "title": item_text,
                "href": full_href,
                "image": item_image
            })
        except Exception as e:
            logging.error(f"Ошибка при обработке элемента: {e}")

    return items

