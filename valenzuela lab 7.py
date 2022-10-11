#Lourie Valenzuela Cano

from urllib import request
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def link_scrape(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    taglist = list()
    for tag in tags:
        t = tag.get('href', None)
        taglist.append(t)
    return taglist

def get_link():
    page = input('Please enter a URL: ' )
    return page

def main():
    tpage = get_link()
    res = requests.get(tpage)
    links = link_scrape(tpage)
    for line in links:
        try:
            request = requests.get(line)
            print(str(line) + ' =====  ' + str(request))
        except Exception as exc:
            print(str(line) + ' bad link')

main()