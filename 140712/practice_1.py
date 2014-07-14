import random

u = 45
a = random.randint(1,45)
list = [a]
for index in range(1,6):
	while a in list:
		a = random.randint(1,45)
	list.append(a)
list.sort()
print list