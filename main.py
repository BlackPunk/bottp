import requests, os
from bs4 import BeautifulSoup

urls = [
    'https://informatics.labs.telkomuniversity.ac.id/category/praktikum/pemrograman-web/',
    'https://informatics.labs.telkomuniversity.ac.id/category/praktikum/analisis-perancangan-perangkat-lunak/'
]
path = os.getcwd()
if "log" not in os.listdir(path):
    os.mkdir('log')
os.chdir(path+"/log")

def getData(linkTP):
    pageTp = requests.get(linkTP)
    soup = BeautifulSoup(pageTp.content, 'html.parser')
    linkKumpul = soup.find(class_='entry-content').find_all('a')[-2]['href']
    linkSoal = soup.find(class_='entry-content').find_all('a')[-1]['href']
    print(f'Halaman TP : {linkTP}\nLink Pengumpulan : {linkKumpul}\nLink Soal : {linkSoal}\n')
    return linkKumpul, linkSoal

def inisialisasi(s,kategori):
    articles = s.find_all('article')
    os.mkdir(kategori)
    os.chdir(kategori)
    print("> Memulai Inisialisasi TP Praktikum {0}\n".format(kategori))
    for article in articles:
        judul = article.find('h2', class_='entry-title').text
        if ("TP MODUL" in judul) and ("INT" not in judul):
            day = article.find('span', class_='day').text.strip()
            month = article.find('span', class_='month').text.strip()
            year = article.find('span', class_='year').text.strip()
            linkTp = article.find('h2', class_='entry-title').find('a')['href']
            linkKumpul, linkSoal = getData(linkTp)
            with open(f'{judul} ({day}-{month}-{year}).txt', 'w+') as f:
                f.write(f'Halaman TP : {linkTp}\nLink Kumpul : {linkKumpul}\nLink Soal : {linkSoal}')
    print(f'> Inisisialisasi selesai.\n')

def bacaHalaman(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    kategori = soup.find('a', href=url).text
    if kategori not in os.listdir():
        inisialisasi(soup, kategori)
    else:
        os.chdir(kategori)
        judul = soup.find('h2', class_="entry-title")
        logJudul = '\n'.join(os.listdir())
        if (judul.text in logJudul) and ("INT" not in judul.text) and ("TP MODUL" in judul.text):
            linkTp = judul.find('a')['href']
            linkKumpul, linkSoal = getData(linkTp)

for url in urls:
    bacaHalaman(url)
    os.chdir(path + "/log")