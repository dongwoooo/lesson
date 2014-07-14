# -*- coding: UTF-8 -*-
import random
C = 0
while C == 0:
	A = 0
	ans_A = raw_input("가위, 바위, 보 중에 골라 : ")
	while A == 0:
		if ans_A == "가위":
			A = 1;
		elif ans_A == "바위":
			A = 2;
		elif ans_A == "보":
			A = 3;
		else:
			ans_A = raw_input("가위, 바위, 보 중에 골라. 다시: ")
	
	B = random.randint(1,3)
	if B == 1:
		ans_B = "가위"
	elif B == 2:
		ans_B = "바위"
	else:
		ans_B = "보"

	print "니가낸거 : %s" % (ans_A)
	print "컴터가낸거 : %s" % (ans_B)
	if A == B:
		print "무승부"
	elif (A == 1 and B == 2) or (A == 2 and B == 3) or (A == 3 and B == 1):
		print "니가 졌음"
	else:
		print "니가 이김"

	ans_C = raw_input("한번 더 할래? [응 / 아니] : ")
	D = 0
	while D == 0:
		if ans_C == "응":
			C = 0
			D = 1
		elif ans_C == "아니":
			print "잘가"
			C = 1
			D = 1
		else:
			ans_C = raw_input("응/아니 중에 하라니까. 다시 : ")