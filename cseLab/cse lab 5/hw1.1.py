def is_prime(n):
	for x in range(2, int(n ** 0.5 + 1)):
		if n % x == 0:
			return False
	return True

n = int(input())
prime_check = is_prime(n)
print(prime_check)