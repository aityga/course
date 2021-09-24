from bs4 import BeautifulSoup
import requests
import csv

CSV = 'sulpak.csv'
HOST = 'https://www.sulpak.kg'
URL = 'https://www.sulpak.kg/f/noutbuki'
HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

def get_html(URL, params = ''):
    r = requests.get(URL, headers=HEADERS, params=params, verify=False)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('div', class_='product-container-right-side').find('h3', class_='title').get_text(strip=True),
            'link': HOST + item.find('div', class_='product-container-right-side').find('a').get('href'),
            'price': item.find('div', class_='product-container-right-side').find('div', class_='price').get_text(strip=True),
            'image': HOST + item.find('div', class_='listbox_img pull-left').find('picture').find('img', class_='image-size-cls').get('src')
        })
    return comps

def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['title', 'link', 'price'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['price']])

def pagination():
    PAGINATION = input('which pages: ')
    PAGINATION = int((PAGINATION).strip())
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
        print("error")

pagination()
# from bs4 import BeautifulSoup
# import requests
# import csv
#
# CSV = 'sulpak.csv'
# HOST = 'https://www.sulpak.kg'
# URL = 'https://www.sulpak.kg/f/noutbuki'
# HEADERS = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
#
# def get_html(URL, params = ''):
#     r = requests.get(URL, headers=HEADERS, params=params, verify=False)
#     return r
#
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.findAll('div', class_ = 'goods-tiles')
#     comps = []
#
#     for item in items:
#         comps.append({
#             'Название ноутбука' :
#             item.find('div', class_ = 'product-container-right-side').find('h3',
#             class_='title'),
#
#             'Ссылка на ноутбук' : HOST +
#             item.find('div',
#             class_ = 'product-container-right-side').find('a').get('href'),
#
#             'Цена Ноутбука': item.find('div',
#             class_ = 'product-container-right-side').find('div',
#             class_ = 'price')
#         })
#     return comps
#
# def save(items, path):
#     with open(path, 'a') as file:
#         writer = csv.writer(file, delimiter = ';')
#         writer.writerow(['Название', 'Ссылка','Цена'])
#         for item in items:
#             writer.writerow([item['Название ноутбука'], item['Ссылка на ноутбук'], item['Цена Ноутбука']])
#
# def pagination():
#     PAGINATION = input('Введите кол-во страниц ')
#     PAGINATION = int(PAGINATION.strip())
#     html = get_html(URL)
#     if html.status_code == 200:
#         items = []
#         for page in range(1, PAGINATION):
#             print(f"Страница №{page} готова")
#             html = get_html(URL, params={'page' : page})
#             items.extend(get_content(html.text))
#         save(items, CSV)
#         print("Парсинг готов")
#     else:
#         print("Error")
# pagination()