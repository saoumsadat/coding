class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class ArrayToLinkedList:
	def __init__(self, arr):
		self.head = None
		self.tail = None
		for x in arr:
			if self.head is None:
				self.head = Node(x, None)
				self.tail = self.head
			else:
				n = Node(x, None)
				self.tail.next = n
				self.tail = n
	
	def print_linked_list(self):
		n = self.head
		while n is not None:
			print(n.data)
			n = n.next
		

a = [10, 20, 30, 40, 50]
linked_list = ArrayToLinkedList(a)
linked_list.print_linked_list()



