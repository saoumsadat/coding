n = int(input())
isPrime = True
verdict = "not a prime or perfect"

i = 2
while (i < n // 2):
    if (n % i == 0):
        isPrime = False
        break
    i += 1

sum = 1
if not(isPrime):
    while (i <= n // 2):
        if (n % i == 0):
            sum += i
            # print(i, sum)
        i += 1

if (isPrime):
    verdict = "a prime"
elif (sum == n):
    verdict = "a perfect"

print(f"{n} is {verdict} number")
