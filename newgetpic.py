import requests
from bs4 import BeautifulSoup



aurl='http://www.meitulu.com/item/9921.html'

urllist =['http://www.meitulu.com/item/9921_3.html','http://www.meitulu.com/item/9921_2.html','http://www.meitulu.com/item/9921_3.html','http://www.meitulu.com/item/9921_4.html','http://www.meitulu.com/item/9921_5.html']

for url in urllist:
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    #pic = soup.select('.content')
    pic =  soup.select('center')           ##最外层标签（第三层）
    for link in pic:                       #列表超限
        a = link.select('img')[0]['src']   #中间层IMG，取列表第一个，取内层字典src对应链接 
        b = link.select('img')[0]['alt']
        print (a)
        #print (b)

