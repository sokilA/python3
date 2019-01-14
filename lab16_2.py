#!/usr/bin/env python3

import bs4
import requests
import csv
import re


def write_parsed_page(response, writer):
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    notebooks = soup.find_all(class_='product-block')

    for notebook in notebooks:
        name = notebook.find(class_='model-name').text
        price = notebook.find(class_='price').text
        all_desc = notebook.find_all(class_='short-descr-line')
        desc = '\n'.join([desc.text.strip() for desc in all_desc])
        link = notebook.find(class_='btn')['href']
        if link[0] == '/':
            link = "https://price.ua" + link
        photo_link = notebook.find(class_='photo-wrap').find('img')['src']
        photo_link = f"https:{photo_link}"
        writer.writerow([val_filter(name),
                         val_filter(price),
                         val_filter(desc),
                         val_filter(link),
                         val_filter(photo_link)])


def val_filter(value: str) -> str:
    return value.replace("\'", '').replace("\"", '').replace("\n", ' ')


with open("laptops.csv", 'w', encoding='utf-8') as file:
    url = "https://price.ua/catc839t14/page{}.html?price[min]=10000&price[max]=20000"
    i = 1
    csv_writer = csv.writer(file)
    while True:
        r = requests.get(url=url.format(i))
        page = int(re.search(r'page\d+', r.url).group(0).replace('page', '')) \
            if i != 1 else 1
        if i != page:
            break
        else:
            write_parsed_page(r, csv_writer)
            i += 1
