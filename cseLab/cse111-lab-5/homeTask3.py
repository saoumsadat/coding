class Department():
	def __init__(self, *args):
		self.total_students = 0
		self.avg_students = 0
		if (len(args) == 1):
			if (isinstance(args[0], int)):
				self.sections = args[0]
				self.dept = "ChE Department"
			elif (isinstance(args[0], str)):
				self.sections = 5
				self.dept = args[0]
		elif (len(args) == 2):
			self.sections = args[1]
			self.dept = args[0]
		else:
			self.sections = 5
			self.dept = "ChE Department"

		print(f"{self.dept} has {self.sections} sections.")
	
	def add_students(self, *args):
		if (len(args) == self.sections):
			for n in args:
				self.total_students += n
			self.avg_students = round(self.total_students / len(args), 2)
			print(f"The {self.dept} has an average of {self.avg_students} students in each section.")
		else:
			print(f"The {self.dept} doesn't have {len(args)} sections.")
	
	def merge_Department(self, *depts):
		for dept in depts:
			self.total_students += dept.avg_students * dept.sections
			self.avg_students = round(self.total_students / self.sections, 2)
			print(f"{dept.dept} is merged to {self.dept}.")
		return (f"Now the {self.dept} has an average of {self.avg_students} students in each section.")


d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))