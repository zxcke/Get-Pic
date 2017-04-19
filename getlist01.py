import requests
from bs4 import BeautifulSoup
#import re

##get source data
url = 'http://127.0.0.1/index.html'
res = requests.get(url)
res.enconding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')
lists = soup.select('#pages a')

#get link
firstlink = lists[0].get('href')
secondlink = lists[1].get('href')
lastlink = lists[-2].get('href')

#get link num
a = secondlink.split("_",2)                              
b = a[1].split(".",2)                    
#ab = a[0]+'_'+b[0]+'.html'
c = lastlink.split("_",2)                                 
d = c[1].split(".",2)

#change to int
ir = int(b[0])
xr = int(d[0])

##add to list
alllink = []                                            
alllink.append(firstlink)                                                      
while( ir < xr ):
    alllink.append(a[0]+'_'+str(ir)+'.html')             
    ir = ir+1
#print(secondlink)
alllink.append(lastlink)                                 

##print test
for lis in alllink:
    print(lis)


