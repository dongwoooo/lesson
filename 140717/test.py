#-*- coding:utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup

data = urlopen('http://www.huffingtonpost.com/').read()
soup = BeautifulSoup(data)
for hi in soup.findAll('img'):
	print hi['src']
print soup.select('h1 a')[0].text