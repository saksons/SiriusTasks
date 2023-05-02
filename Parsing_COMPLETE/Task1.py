"""
Соберите данные с чартов яндекс музыки https://music.yandex.ru/chart
Внимательно изучите источник, посмотрите как именно на сайт приходит информация.
Сохраните данные в json файл в формате:
{
место в чарте: (исполнитель,трек)
}
"""

import requests
from bs4 import BeautifulSoup as bs
import json

response = requests.get("https://music.yandex.ru/chart")

a = {}

soup = bs(response.text, "lxml")
for i in range(100):
    treck = soup.findAll("div", class_="d-track typo-track d-track_selectable d-track_with-cover d-track_with-chart")[i].findNext("div", class_="d-track__overflowable-column").findNext("div", class_="d-track__overflowable-wrapper deco-typo-secondary").findNext("div", class_="d-track__name").findNext('a', class_="d-track__title deco-link deco-link_stronger").text.lstrip().rstrip()
    name = soup.findAll("div", class_="d-track typo-track d-track_selectable d-track_with-cover d-track_with-chart")[i].findNext("div", class_="d-track__overflowable-column").findNext("div", class_="d-track__overflowable-wrapper deco-typo-secondary").findNext("div", class_="d-track__meta").findNext('a', class_="deco-link deco-link_muted").text.lstrip().rstrip()
    a[i+1] = (name, treck)

with open("yandex_music.json", 'w', encoding="UTF-8") as file:
    file.write(json.dumps(a, indent=4, ensure_ascii=False))