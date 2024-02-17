#part A
#creating class
class box:
	def __init__(self, dim_arr):
		print("Creating a Box!")
		self.height = dim_arr[0]
		self.width = dim_arr[1]
		self.breadth = dim_arr[2]

#driver code
print("Box 1")
b1 = box([10,10,10])
print("=========================")
print("Height:", b1.height)
print("Width:", b1.width)
print("Breadth:", b1.breadth)
volume = b1.height * b1.width * b1.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
print("Height:", b3.height)
print("Width:", b3.width)
print("Breadth:", b3.breadth)
volume = b3.height * b3.width * b3.breadth
print(f"Volume of the box is {volume} cubic units.")

#part B
one = (b3 == b2)

b3.width = 100
two = (b3 == b2)
print(one, two)
print(b2.width)