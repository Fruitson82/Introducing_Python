#4.1
guess_me = 7

if guess_me < 7:
	print("too low")
elif guess_me > 7:
	print("too high")
else:
	print("just right")
print("======================================")

#4.2
guess_me = 7
start = 1

while True:
	if start < guess_me:
		print("too low")
	elif start == guess_me:
		print("found it!")
		break
	else:
		print("oops")
		break
	start += 1
print("======================================")

#4.3
list_value = [3, 2, 1, 0]
for value in list_value:
	print(value)
print("======================================")

#4.4
list_value = []
for value in range(10):
	if (value % 2) == 0 and value != 0:
		list_value.append(value)
print(list_value)
print("======================================")
