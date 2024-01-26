def power(a, n):
	if n == 1:
		return a
	else:
		return a * power(a, n - 1)

a = int(input())
n = int(input())

print(power(a, n))