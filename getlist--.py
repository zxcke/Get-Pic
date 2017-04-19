import requests
from bs4 import BeautifulSoup

url = raw_input('type Url:')
#url = 'http://www.meitulu.com/item/8696.html'
#http://www.meitulu.com/item/3499.html
ress = requests.get(url)
ress.encoding = 'utf-8'
soup = BeautifulSoup(ress.text,'html.parser')

for link in soup.select('a'):
    item = 'http://www.meitulu.com/item/'
    aa = link.get('href')
    if aa[0:28] == item:
        ress2 = requests.get(aa)
        ress2.encoding = 'utf-8'
        soup2 = BeautifulSoup(ress2.text,'html.parser')
        #print (soup2)
        #soup2 = soup2.find_all('img') 
        soup2 = soup2.find_all("img",class_="content_img")
        for list in soup2:    
            linkk = list.get('src')
            print (linkk)



