import requests
from bs4 import BeautifulSoup



aurl='http://www.meitulu.com/item/9921.html'

urllist =['http://www.meitulu.com/item/9921_3.html','http://www.meitulu.com/item/9921_2.html','http://www.meitulu.com/item/9921_3.html','http://www.meitulu.com/item/9921_4.html','http://www.meitulu.com/item/9921_5.html']

for url in urllist:
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    #pic = soup.select('.content')
    pic =  soup.select('center')           ##������ǩ�������㣩
    for link in pic:                       #�б���
        a = link.select('img')[0]['src']   #�м��IMG��ȡ�б��һ����ȡ�ڲ��ֵ�src��Ӧ���� 
        b = link.select('img')[0]['alt']
        print (a)
        #print (b)

