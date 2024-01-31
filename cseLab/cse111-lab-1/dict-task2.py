d = dict()
while(True):
  n = input()
  if n == 'STOP':
    break
  elif n in d.keys():
    d[n] += 1
  else:
    d[n] = 1

for k in d.keys():
  print(f"{k} - {d[k]} times")