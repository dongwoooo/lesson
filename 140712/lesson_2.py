#-*- coding:utf-8 -*-
value = raw_input("어디까지 출력하고 싶으냐.\n")
value = int(value)

if value < 0 :
	print "양수 넣어라."
else :
	int_val = int(value)
	while int_val >= 0:
		for index in range(-4,1):
			if int_val + index >= 0:
				print int_val + index,
		int_val -= 5
		print
	else:
		print "다했다. 꺼라."