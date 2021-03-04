import re
import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm

nbPages = 549
page_url = "https://www.mubawab.ma/fr/sc/appartements-a-louer:o:n:p:"
regex = re.compile(r'[\n,\r,\t]')


# creating function that get articles url
def get_cards_url(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = [tag['linkref'] for tag in soup.find_all('li', class_="basicList", linkref=True)]
    return urls


# creating function that get the needed data from each article web page
def get_data_from_cards(card_link):
    global regex
    global info
    card = {
        'prix en MAD': '',
        'emplacement': '',
        'surface en m²': '',
        'nombre des pièces': '',
        'nombre des chambres': '',
        'numéro d\'étage': ''
    }
    page = requests.get(card_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        info = list(filter(lambda x: x != '', " ".join(
            set([regex.sub(" ", l.text) for l in soup.find_all('span', class_="tagProp")])).split()))
    except:
        return card
    try:
        localisation = regex.sub("", soup.find('p', class_="darkblue inBlock float-right floatL").get_text())
    except:
        localisation = None
    try:
        price = int(
            re.compile(r'[^0-9]').sub("", soup.find("h3", class_="orangeText col-2 fSize14 sMargTop").get_text()))
    except:
        price = 0

    # creating a nested function that collecte data using a keyword
    def get_info(card_key):
        global info
        keyword_switcher = {
            'nombre des chambres': 'Chambres',
            'surface en m²': 'm²',
            'nombre des pièces': 'Pièces',
            'numéro d\'étage': 'étage'
        }
        keyword = keyword_switcher[card_key]
        try:
            i = info.index(keyword)
            card[card_key] = int(re.compile(r'[^0-9]').sub("", info[i - 1]))
        except ValueError:
            try:
                i = info.index(keyword.rstrip('s'))
                card[card_key] = int(re.compile(r'[^0-9]').sub("", info[i - 1]))
            except ValueError:
                card[card_key] = None

    card['prix en MAD'] = price
    card['emplacement'] = localisation
    get_info('surface en m²')
    get_info('nombre des pièces')
    get_info('nombre des chambres')
    get_info('numéro d\'étage')
    return card


print('This web scrapper was created by : Badreddine MOUHASSINE')
with open('Location_Data.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['prix en MAD',
                                                 'emplacement',
                                                 'surface en m²',
                                                 'nombre des pièces',
                                                 'nombre des chambres',
                                                 "numéro d'étage"])
    writer.writeheader()
    for i in range(nbPages):
        print("collectting data from page ", i + 1)
        with tqdm(total=33) as pbar1:
            for link in get_cards_url(page_url + str(i + 1)):
                try:
                    writer.writerow(get_data_from_cards(link))
                except:
                    pass
                pbar1.update(1)
print('*' * 30)
print('*' * 5 + 'Data were being collected from the website and stored in Location_Data.csv file' + '*' * 5)
print('This web scrapper was created by : Badreddine MOUHASSINE')
