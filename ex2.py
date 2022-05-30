from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html=urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs=BeautifulSoup(html,'html.parser')
nameList = bs.findAll('span',{'class':'green'})
for name in nameList:
    print(name.get_text())

html=urlopen('https://www.pythonscraping.com/pages/page3.html')
bs=BeautifulSoup(html,'html.parser')
images=bs.findAll('img',{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})

for image in images:
    print(image['src'])