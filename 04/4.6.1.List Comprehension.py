number_list1 = []
number_list1.append(1)
number_list1.append(2)
number_list1.append(3)
number_list1.append(4)
number_list1.append(5)
print("number_list1: ", number_list1)

number_list2 = []
for number in range(1, 6):
	number_list2.append(number)
print("number_list2: ", number_list2)

number_list3 = list(range(1, 6))
print("number_list3: ", number_list3)

number_list4 = [number for number in range(1, 6)]
print("number_list4: ", number_list4);

number_list5 = [number-1 for number in range(1, 6)]
print("number_list5: ", number_list5)

a_list = [number for number in range(1, 6) if number % 2 == 1]
print("a_list: ", a_list)

a_list2 = []
for number in range(1, 6):
	if number % 2 == 1:
		a_list2.append(number)
print("a_list2: ", a_list2)

rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
print("cells: ", cells)