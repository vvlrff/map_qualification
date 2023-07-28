from bs4 import BeautifulSoup
import requests


def get_news_theguardian():
    url = 'https://www.theguardian.com/world'

    headers = {
        'Accept': '*/*', 
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.3.799 Yowser/2.5 Safari/537.36'
    }

    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    items = []

    allHrefs = soup.find_all(class_="dcr-lv2v9o")
    allText = soup.find_all(class_="show-underline dcr-adlhb4")

    max_len = max(len(allHrefs), len(allText))

    for i in range(max_len):
        try:
            itemText = allText[i].text
            itemHref = allHrefs[i].get('href')
            fullHref = "https://www.theguardian.com" + str(itemHref)
            items.append(
                {
                    "title": itemText,
                    "href": fullHref
                }
            )
        except Exception:
            print("error")


    return items
