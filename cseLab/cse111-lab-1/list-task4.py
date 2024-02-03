def strToList(s):
	num_str = ''
	arr = []
	for x in range(0, len(s)):
		if s[x] == ' ':
			arr.append(int(num_str))
			num_str = ''
		else:
			num_str += s[x]
		if x == (len(s) - 1):
			arr.append(int(num_str))
			break
	return arr


while(True):
	s = input()
	v = ''
	if s == "STOP":
		break

	arr = strToList(s)
	N = len(arr)

	diff = 0
	for x in range(1, N):
		diff = arr[x] - arr[x - 1]

		if diff < 0:
			diff = diff * (-1)

		if diff < N:
			v = "UB Jumper"
		else:
			v = "Not UB Jumper"
					
	print(v)