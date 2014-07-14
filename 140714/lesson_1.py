with file("text.txt", "r") as text:
# text = file("text.txt", "r")
	for line in text:
		print line,
	text.close()