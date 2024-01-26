def recursive_summation(st, n):
	if st > n:
		return 0
	else:
		return st + recursive_summation(st + 1, n)
	
print(recursive_summation(1, 12))