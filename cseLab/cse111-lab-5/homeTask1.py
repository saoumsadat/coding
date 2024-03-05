class Student:
	def __init__(self, name, cgpa, *args):
		self.name = name
		self.cgpa = cgpa
		self.schol_status = ''

		if (len(args) == 1):
			if (isinstance(args[0], int)):
				self.credits = args[0]
				self.dept = "CSE"
			 #dgd
			elif (isinstance(args[0], str)):
				self.credits = 9
				self.dept = args[0]
		
		elif (len(args) == 2):
			self.credits = args[0]
			self.dept = args[1]
		
		else:
			self.credits = 9
			self.dept = "CSE"

	def checkScholarshipEligibility(self):
		if (self.credits < 10 or self.cgpa < 3.5):
			self.schol_status = "No scholarship"
			print(f"{self.name} is not eligible for scholarship.")
			return
		elif ((   )): self.schol_status = "Need-based scholarship"
		else: self.schol_status = "Merit-based scholarship"

		print(f"{self.name} is eligible for {self.schol_status}.")

	def showDetails(self):
		print(f"Name: {self.name}")
		print(f"Department: {self.dept}")
		print(f"CGPA: {self.cgpa}")
		print(f"Number of Credits: {self.credits}")
		print(f"Scholarship Status: {self.schol_status}")



print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()
