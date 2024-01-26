myList = [10, 1, 4, 3, 8, 2, 4, 3, 5, 8, "done"]
index1, index2 = 0, 0
index1 = 1
while(index1<10):
  while(index2<index1):
    myList[index1] = myList[index1]+myList[index2]-index1
    index2 = index2+1
  print(myList[index1])
  index1 = index1+1
print(myList[-1:])

