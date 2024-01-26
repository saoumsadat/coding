def is_prime(n):
	for x in range(2, int(n ** 0.5 + 1)):
		if n % x == 0:
			return False
	return True

def is_perfect(n):
	sum = 1
	for x in range(2, int(n ** 0.5) + 1):
		if n % x == 0:
			sum += x + (n // x)
	if sum == n:
		return True
	return False

def special_sum(n):
	sum = 0
	for x in range(2, n):
		if is_perfect(x) or is_prime(x):
			sum += x
	return sum

n = int(input())
result = special_sum(n)
print(result)