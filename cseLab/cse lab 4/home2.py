s = input()
sec_start = 0
comma_index = 0
for i in range(0, len(s)):
    if s[i] == ",":
        comma_index = i
        sec_start = i + 2

part1 = s[0:comma_index]
part2 = s[sec_start:]

# print(part1, part2)
new_s = ""

i = 0
while (i < len(part1) and i < len(part2)):
    new_s += part1[i] + part2[i]
    i += 1

if (i < len(part1)):
    new_s += part1[i:]
else:
    new_s += part2[i:]

print(new_s)