text = file("treasure_map.txt", "r+")
for line in text:
	print line[int(filter(lambda x: x in '0123456789', line))],
text.close()
print
txt = file("treasure_map.txt", "r+")
for line in txt:
	if line.find("!@#$%") >= 0:
		print line[line.find("!@#$%") + len("!@#$%")],