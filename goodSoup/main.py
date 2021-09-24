from bs4 import BeautifulSoup
import requests
import csv

CSV = 'kivano.csv'
HOST = 'https://www.kivano.kg'
URL = 'https://www.kivano.kg/kolonki-portativnye'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

def get_html(URL, params = ''):
    r = requests.get(URL, headers=HEADERS, params=params, verify=False)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='item product_listbox oh')
    comps = []

    for item in items:
        comps.append({
            'name': item.find('div', class_='pull-right rel').find('a', target='_blank'),
            'link': HOST + item.find('div', class_='pull-right rel').find('a').get('href'),
            'price': item.find('div', class_='motive_box pull-right').find('div', class_='listbox_price text-center'),
            'image': HOST + item.find('div', class_='listbox_img pull-left').find('a').find('img').get('src')
        })
    return comps

def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['name', 'link', 'price', 'image'])
        for item in items:
            writer.writerow([item['name'], item['link'], item['price'], item['image']])

def pagination():
    PAGINATION = input('which pages: ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        items = []
        for page in range(1, PAGINATION):
            print(f"page №{page} ready")
            html = get_html(URL, params={'page': page})
            items.extend(get_content(html.text))
        save(items, CSV)
        print("parsing")
    else:
        print("Error")
pagination()