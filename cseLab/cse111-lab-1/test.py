# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def strToList(s):
	num_str = ''
	arr = []
	for x in range(0, len(s)):
		if s[x] == ' ' or x == (len(s) - 1):
			if x == (len(s) - 1): 
					num_str += s[x]
			arr.append(int(num_str))
			num_str = ''
		else:
			num_str += s[x]
# 		if x == (len(s) - 1):
# 			arr.append(int(num_str))
# 			break
	return arr


n = int(input())
sum = 0
list_str = ''
for i in range(0, n):
	s = input()
	arr = strToList(s)
	temp_sum = 0
	for j in range(0, len(arr)):
		temp_sum += arr[j]
	if temp_sum > sum:
		sum = temp_sum
		list_str = str(arr)

print(sum)
print(list_str)