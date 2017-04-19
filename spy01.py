import requests
from bs4 import BeautifulSoup

url = raw_input('type Url:')
#url = 'http://www.meitulu.com/item/8696.html'
ress = requests.get(url)
ress.encoding = 'utf-8'

soup = BeautifulSoup(ress.text,'html.parser')
#print (soup)
#soup = soup.find_all('img') 
soup = soup.find_all("img",class_="content_img")
for list in soup:    
    #link = list.find('img')
    link = list.get('src')
    #print (type(link))
    print (link)
