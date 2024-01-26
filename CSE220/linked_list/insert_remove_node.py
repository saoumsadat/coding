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

	def insert_node(self, index, data):
		new_node = Node(data, None)
		if index == 0:
			new_node.next = self.head
			self.head = new_node
		else:
			after = self.node_at(index)
			before = self.node_at(index - 1)
			before.next = new_node
			new_node.next = after

	def remove_node(self, index):
		if index == 0:
			to_remove = self.head;	
			self.head = self.head.next;
			to_remove.next = None;	
		else:
			to_remove = self.node_at(index)
			before = self.node_at(index - 1)
			before.next = to_remove.next
			to_remove.next = None

a = [10, 20, 30, 40, 50]
#add 5 at index = 0
#add 25 at index = 2
#remove node at index = 0
#remove node at index = 2

linked_list = ArrayToLinkedList(a)

linked_list.insert_node(0, 5)
linked_list.insert_node(2, 25)
linked_list.print_linked_list()

print()

linked_list.remove_node(0)
linked_list.remove_node(2)
linked_list.print_linked_list()

