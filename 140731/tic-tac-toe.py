list = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def win_check(list, player):
	win = False
	for i in range(3):
		if (list[i][0] == list[i][1] == list[i][2] == player) or (list[0][i] == list[1][i] == list[2][i] == player) or (list [0][0] == list [1][1] == list [2][2] == player) or (list [0][2] == list [1][1] == list [2][0] == player):
			win = True

	return win

def print_list(list):
	for row in list:
		for item in row:
			print item,
		print
	print

win = False
n = 0

while (win == False) and (n < 9):
	player = 'X' if n%2 else 'O' 
	while True:
		input_x = raw_input("Type x : ")
		while input_x not in '012':
			input_x = raw_input("Type in 0 or 1 or 2 : ")
		input_x = int(input_x)

		input_y = raw_input("Type y : ")
		while input_y not in '012':
			input_y = raw_input("Type in 0 or 1 or 2 : ")
		input_y = int(input_y)

		if list[input_y][input_x] == ' ':
			break
		else:
			print("That spot is already taken. Pick another spot.\n")
	list[input_y][input_x] = player
	n += 1
	print_list(list)
	win = win_check(list, player)

if win:
	print("Winner is %s." % (player))
else:
	print("Draw.")