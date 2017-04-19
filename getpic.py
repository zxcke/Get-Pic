#coding = UTF-8
#!c:/Python27/python.exe
'''
file: getpic.py



'''


import requests
import wget
import time
from bs4 import BeautifulSoup


#url = raw_input("type url: ")
url ='http://www.meitulu.com/item/9919.html'


headers = {
    'Host': 'blog.csdn.net',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.baidu.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

response = requests.get(url,headers).text

# response = response.encode('utf-8')
# print response

bsObj = BeautifulSoup(response,'html.parser')

#bsObj = bsObj.encode('utf-8')

alink = bsObj.select('img')

for link in alink:
    print (link['src'])
    #wget.download((link['src']))
    #time.sleep(3)


#print (bsObj)

#bsObj = bsObj.find_all('div',{'class':'content'})

#bsObj =  bsObj.find_all('img')

#print bsObj




'''
for tag in bsObj:

    div_tag = tag.contents[].get_src()

    name = div_tag.strip('\n').replace(' ','') +'\n'

    print(name)
'''
