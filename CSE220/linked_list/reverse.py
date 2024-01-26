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
				self.head = Node(x, None);
				self.tail = self.head
			else:
				n = Node(x, None);
				self.tail.next = n
				self.tail = n
	
	def print_linked_list(self):
		n = self.head
		while n is not None:
			print(n.data)
			n = n.next

	def reverse(self, direction):
		if direction == 'out':
			n = self.head
			next = None
			while n is not None:
				new_n = Node(n.data, next)
				self.head = new_n
				next = new_n
				n = n.next

		elif direction == 'in':
			n = self.head
			next = None
			while True:
				if not(n.next):
					n.next = next
					break
				self.head = n.next
				n.next = next
				next = n
				n = self.head


a = [10, 20, 30, 40, 50]
linked_list = ArrayToLinkedList(a)
linked_list.reverse('in')
ArrayToLinkedList.print_linked_list(linked_list)