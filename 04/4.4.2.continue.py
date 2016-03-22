# -*- coding:utf-8 -*-
while True:
	value = input("Integer, please [q to quit]: ")
	print ("value: ", value)
	if value == 'q': #종료
		break
	number = int(value)
	if number % 2 == 0: # 짝수
		continue
	print (number, "squared is ", number*number)