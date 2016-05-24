number_thing = (number for number in range(1, 6))
print("type(number_thing): ", type(number_thing))


for number in number_thing:
	print(number)

number_list = list(number_thing)
print("number_list: ", number_list)