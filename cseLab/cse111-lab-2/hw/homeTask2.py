def is_james_bond(arr):
	zero_count = 0
	for i in range(0, len(arr)):
		if arr[i] == 0: zero_count += 1
		elif arr[i] == 7 and zero_count >= 2: return True
		elif arr[i] == 7: return False 
	return False

result = is_james_bond( [1, 0, 2, 0, 4, 7, 5] )
print(result)