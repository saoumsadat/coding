def is_perfect(n):
	sum = 1
	for x in range(2, int(n ** 0.5) + 1):
		if n % x == 0:
			sum += x + (n // x)
	if sum == n:
		return True
	return False

n = int(input())
perfect_check = is_perfect(n)
print(perfect_check)