#-*- coding:utf-8 -*-
from urllib import urlopen
from bs4 import BeautifulSoup
import os
import codecs

if not os.path.exists("html"):
			os.makedirs("html")

data = urlopen('http://openapi.naver.com/search?key=160ed1198e4faee56344a9625698d83e&query=%EC%9E%90%EC%99%B8%EC%84%A0+%EC%B0%A8%EB%8B%A8&target=news&start=1&display=20&sort=sim')
soup_data = BeautifulSoup(data)

# 파일 이름을 위한 변수 num 선언 및 초기화
num = 0
for head in soup_data.findAll('link'):
	# item 안의 기사 주소들만 선택하여 그 주소의 데이터를 받아옴
	if head.parent.name == 'item':
		num += 1
		url = head.text
		site = urlopen(url)
		soup_each = BeautifulSoup(site)

		# 파일 생성 및 쓰기
		file = open("html" + "\\" + str(num) + ".html", "w")
		file.write(soup_each.encode('utf-8'))
		file.close()