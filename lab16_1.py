#!/usr/bin/env/python3

import requests
import bs4
import csv

response = requests.get('http://www.codeabbey.com/index/user_ranking')
soup = bs4.BeautifulSoup(response.content, features='lxml')
table = soup.find_all('tr')
with open('result.csv', 'w') as file:
    file.write('position,username,language,rank,enlightenment,solved\n')
    for tr in table[2:]:
        td = tr.findAll('td')
        file.write(td[0].text)
        file.write(',')
        file.write(td[2].find('a').text)
        file.write(',')
        file.write(td[3].text)
        file.write(',')
        file.write(td[4].find('span').text)
        file.write(',')
        file.write(td[5].text.replace(',', '.'))
        file.write(',')
        file.write(td[6].text)
file.write('\n')
