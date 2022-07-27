import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}


def get_url():
    for count in range(1, 3):


        url = f'https://cars.av.by/filter?page={count}'
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        cars = soup.find_all('div', class_='listing-item')

        for i in cars:
            card = 'https://cars.av.by' + i.find('a').get('href')

            yield card


def poisk():
    for card in get_url():
        sleep(2)
        res = requests.get(card, headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')
        cars = soup.find('div', class_='card')
        name = cars.find('h1', class_='card__title').text
        params = cars.find('div', class_='card__params').text
        price = cars.find('div', class_='card__price').text
        location = cars.find('div', class_='card__location').text
        foto = cars.find('img').get('data-src')

        yield name, params, price, location, foto, card
