#-*- coding:utf-8 -*-
import random
import os
import time

# 로그 임시 저장 장소 생성
tmp = ""

# 도입부 제목 프린트
print "<< Numeric Baseball >>\n"
tmp += "<< Numeric Baseball >>\n\n"

# 게임 파트 루프
terminate = False
while terminate == False:
	# 정답(ans_real) 생성
	ans_real = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	random.shuffle(ans_real)
	for index in range(6):
		ans_real.pop()

	# 시도 횟수 초기화
	count = 0

	# 게임 한 판
	success = False
	while success == False:
		while True:
			# 사용자의 입력을 받아 그것을 리스트로 변환
			num_input = 0
			while num_input == 0:
				ans = raw_input("What is your 4-digit guess? : ")
				tmp += "What is your 4-digit guess? : "
				ans_my = list(ans)
				for item in ans_my:
					tmp += "%s" % item
				
				# 정수인지 아닌지 확인
				right_num = 0
				for item in ans_my:
					if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
						print "Please Enter in integer.\n"
						tmp += "\nPlease Enter in integer.\n\n"
						break
					elif right_num == 3:
						num_input = 1
					right_num += 1


			# 중복된 수 확인
			if len(list(set(ans_my))) != 4:
				print "Please Enter 4 distict digit number.\n"
				tmp += "\nPlease Enter 4 distict digit number.\n\n"
			
			# 제대로 쳤을 경우 스트라이크 확인으로 넘어감
			else:
				break

		# 스트라이크와 볼 수 초기화
		str = 0
		ball = 0

		# 스트라이크와 볼 수 계산
		for index in range(4):
			if ans_my[index] == ans_real[index]:
				str += 1
			if ans_my[index] in ans_real:
				ball += 1
		ball -= str

		# 스트라이크와 볼 수 출력
		print ">> %dS %dB\n" % (str, ball)
		tmp += "\n>> %dS %dB\n\n" % (str, ball)
		count += 1

		# 스트라이크가 4일 경우(맞춘 경우) 시도 횟수 보여주는 부분
		if str == 4:
			print "You got it in %d guesses!\n" % (count)
			tmp += "You got it in %d guesses!\n\n" % (count)
			success = True

		# 스트라이크가 4가 아닐 경우 다시 시도
		else:
			pass
	
	# 한 판 더 할 것인지 묻는 단계
	more = raw_input("Wanna play more? [y/n] : ")
	tmp += "Wanna play more? [y/n] : %s\n" % more
	while True:
		if more == "y":
			break
		elif more == "n":
			terminate = True
			break
		else:
			more = raw_input("Type in y or n: ")
			tmp += "Type in y or n: %s\n" % more

# 저장 여부 확인
log_save = raw_input("Do you want to save the log? [y/n] : ")
tmp += "Do you want to save the log? [y/n] : %s\n" % log_save

# 저장
while True:
	if log_save == "y":
		if not os.path.exists("baseball_log"):
			os.makedirs("baseball_log")
		date = time.strftime("%Y%m%d%H%M%S.txt")
		location = os.path.join("baseball_log", date + ".txt")
		file = open(location, "w")
		file.write(tmp)
		file.close
		break
	elif log_save == "n":
		break
	else:
		log_save = raw_input("Type in y or n : ")
		tmp += "Type in y or n: %s\n" % log_save