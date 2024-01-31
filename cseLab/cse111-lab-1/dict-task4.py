s = input()
d = dict()
for x in s:
  if x == ' ':
    continue
  elif (x >= 'A' and x <= 'Z'):
    x = chr(ord(x) + 32)
  
  if x in d.keys():
    d[x] += 1
  else:
    d[x] = 1
    
print(d)

