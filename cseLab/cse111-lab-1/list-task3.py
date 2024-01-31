def strToList(s):
    num_str = ''
    arr = []
    for x in range(0, len(s)):
        if s[x] == ' ':
            arr.append(int(num_str))
            num_str = ''
        else:
            num_str += s[x]
        if x == (len(s) - 1):
            arr.append(int(num_str))
            break
    return arr

s1 = input()
arr1 = strToList(s1)
s2 = input()
arr2 = strToList(s2)

ans_list = []
for i in range(0, len(arr1)):
    for j in range(0, len(arr2)):
        product = arr1[i] * arr2[j]
        ans_list.append(product)

print(ans_list)