def invertDict(d):
  new_d = {}
  for k in d.keys():
    val = d[k]
    if val not in new_d.keys():
      new_d[val] = [k]
    else:
      new_d[val].append(k)
  return new_d

d = {
  'key1' : 'value1',
  'key2' : 'value2',
  'key3' : 'value1'
}

new_d = invertDict(d)
print(new_d)
