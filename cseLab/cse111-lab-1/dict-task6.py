keymap = {
  '1': '.,?!:',
  '2': 'abc',
  '3': 'def',
  '4': 'ghi',
  '5': 'jkl',
  '6': 'mno',
  '7': 'pqrs',
  '8': 'tuv',
  '9': 'wxyz',
  '0': ' '
}

s = input()
for x in s:
  if x >= 'A' and x <= 'Z':
    x = chr(ord(x) + 32)
  
  for k in keymap.keys():
    if x in keymap[k]:
      print(k * (keymap[k].index(x) + 1), end="")

print()