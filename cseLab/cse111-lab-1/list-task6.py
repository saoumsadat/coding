def strToList(s):
	num_str = ''
	arr = []
	for x in range(0, len(s)):
		if s[x] == ' ':
			arr.append(int(num_str))
			num_str = ''
		else:
			num_str += s[x]

		if x == (len(s) - 1) and s[x] != ' ':
			arr.append(int(num_str))
			break
	return arr

s1 = input()
arr1 = strToList(s1)
n = arr1[0]
k = arr1[1]

s2 = input()
arr2 = strToList(s2)
# print(arr2)
member = 0
for i in range(0, n):
	if (arr2[i] + k) <= 5:
		member += 1

team = member // 3
print(team)