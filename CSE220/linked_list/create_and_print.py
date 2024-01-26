class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

#creating nodes
n1 = Node(10, None)
n2 = Node(20, None)
n3 = Node(30, None)
n4 = Node(40, None)

#linking nodes
n1.next = n2
n2.next = n3
n3.next = n4

#printing linked list
n = n1
while n is not None:
	print(n.data)
	n = n.next
	