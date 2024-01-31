def makeDictFromWord():
  s = input()
  d = dict()
  for x in s:
    if x >= 'A' and x <= 'Z':
      x = chr(ord(x) + 32)
    
    if x in d.keys():
      d[x] += 1
    else:
      d[x] = 1
  
  return d

d1 = makeDictFromWord()
d2 = makeDictFromWord()

print(d1)
print(d2)

if d1 == d2:
  print("Those strings are anagrams")
else:
  print("Those strings are not anagrams")