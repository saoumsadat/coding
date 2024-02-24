class GreenPhone:
	def __init__(self, name, version, cam_count):
		self.name = name
		self.version = version
		self.numOfCam = cam_count
		if self.name[0] == 'A': self.remUpdate = 2
		elif self.name[0] == 'M': self.remUpdate = 3
		elif self.name[0] == 'U': self.remUpdate = 4
	def updatePhone(self):
		if self.remUpdate > 0:
			self.version += 1
			self.remUpdate -= 1
		else:
			print(f"Your phone Greenphone {self.name} is already up to date.")
			return
		print(f"Your phone Greenphone {self.name} is upgraded to Android Version: {self.version}.")
	def showSpecification(self):
		print("Your Company: GreenPhone")
		print("Model Name:", self.name)
		print("Android Version:", self.version)
		print("Number of Cameras:", self.numOfCam)

print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()
