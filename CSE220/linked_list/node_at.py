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
	
	def node_at(self, index):
		n = self.head
		count = 0
		while n is not None:
			if index == count:
				return n
			n = n.next
			count += 1

a = [10, 20, 30, 40, 50]
linked_list = ArrayToLinkedList(a)
linked_list.print_linked_list()
print(linked_list.node_at(3).data)