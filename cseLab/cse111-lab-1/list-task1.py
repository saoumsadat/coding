num_list = []
freq_list = []
while (True):
	num = input()
	if num == "STOP":
		break
	elif not (num in num_list):
		num_list.append(num)
		freq_list.append(1)
	else:
		i = num_list.index(num)
		freq_list[i] += 1

for i in range(0, len(num_list)):
	print(f"{num_list[i]} - {freq_list[i]} times")
