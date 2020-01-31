import requests, os, re
from bs4 import BeautifulSoup

urls = [
    'https://informatics.labs.telkomuniversity.ac.id/category/praktikum/pemrograman-web/',
    'https://informatics.labs.telkomuniversity.ac.id/category/praktikum/analisis-perancangan-perangkat-lunak/'
]
path = os.getcwd()
if "log" not in os.listdir(path):
    os.mkdir('log')
os.chdir(path+"/log")

def inisialisasi(s,t):
    articles = s.find_all('article')
    # f = open(t+'.log', 'w+')
    for article in articles:
        day = re.search(r'day">(.*?)</span', article).group(1).strip('\t')
        month = re.search(r'month>(.*?)</span>', article).group(1).strip('\t')
        judul = article.find('h2', class_='entry-title').text
        print(day, judul, judul)
        # f.write(f'{article.text}\n')
    # f.close()
    print(f'Inisisialisasi matkul {t} sukses !')

def bacaHalaman(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find('a', href=url).text
    if title+'.log' not in os.listdir():
        inisialisasi(soup, title)
    else:
        with open(title+'.log', 'r') as f:
            logJudul = f.read()
        print(logJudul)



bacaHalaman(urls[0])


# with open('webpro.log', 'a+') as f:
#     f.write('Test 2\n')


# url = "https://informatics.labs.telkomuniversity.ac.id/category/praktikum/pemrograman-web/"
# page = requests.get(url)
# soup = BeautifulSoup(page.content, "html.parser")
# rs = soup.find_all('article')

# i = 0
# for title in rs:
#     i += 1
#     tag = title.find('h2', class_='entry-title')
#     link = tag.find('a')['href']
#     # if "INT" not in tag.text:
#     print(f'{tag.text} | {link}')
#
# print(f"\nJumlah judul : {i}")
# print(os.listdir(path))