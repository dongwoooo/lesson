def add_strs(strings):
	total = 0;
	for str in strings:
		total += int(str)
	return total

total = add_strs(["1", "2", "3", "4", "5"])
print "Total is " + str(total)