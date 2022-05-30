import imp
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages=set()

def getLinks(pageURL):
    global pages
    html=urlopen('https://en.wikipedia.org'+pageURL)
    bs=BeautifulSoup(html,'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').findAll('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print("This page is missing somethong! No worries though!")
    for link in bs.findAll('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage=link.attrs['href']
                print('------------------\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')