#-*- coding:utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import os
import codecs

os.mkdir("140715")

data_head = urlopen('http://www.huffingtonpost.kr/the-news/2014/07/15/').read()
soup_head = BeautifulSoup(data_head)

for head in soup_head.findAll('h3'):
	title = head.text
	title = title.replace("?","")
	title = title.replace("!","")
	title = title.replace(":","")
	title = title.replace("'","")
	print title
	url = head.a.get('href')
	print url
	data_content = urlopen(url)
	soup_content = BeautifulSoup(data_content)
	article = codecs.open("140715" + "\\" + title + ".txt", "w", "utf-8")
	for content in soup_content.findAll("p"):
		print content.text
		article.write(content.text)
	article.close()