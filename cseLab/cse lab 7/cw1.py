import numpy as np  #as = alias

n = int(input())
ori_arr = np.zeros(n, dtype=int)

for x in range(0, n):
    val = int(input())
    ori_arr[x] = val

print(f"Original Array: {ori_arr}")

res_arr = np.zeros(n + 1, dtype=int)
for x in range(0, n):
    res_arr[x] = ori_arr[x]

m = int(input())

res_arr[len(res_arr) - 1] = m
ori_arr = res_arr
print(f"Resized Array: {ori_arr}")
