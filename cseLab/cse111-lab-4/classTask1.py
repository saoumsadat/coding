class Customer:
	def __init__(self):
		print("Welcome to ABC Memorial Park")
		self.ticketCount = 0
		self.totalPrice = 0

	def buyTicket(self, name, age):
		if self.ticketCount < 3:
			if age > 10: self.totalPrice += 100
			else: self.totalPrice += 50
			self.ticketCount += 1
		else:
			print("You can't buy more than 3 tickets")
			return
		print(f"Successfully purchased a ticket for {name}!")

	def showDetails(self):
		print("Amount of tickets:", self.ticketCount)
		print("Total price:", self.totalPrice)

print('1-------------------------')
customer1 = Customer()
print('2-------------------------')
customer1.buyTicket('Bob', 23)
customer1.buyTicket('Henry', 7)
customer1.buyTicket('Alexa', 30)
customer1.buyTicket('Jonas', 43)
print('3-------------------------')
customer1.showDetails()
print('4-------------------------')
customer2 = Customer()
print('5-------------------------')
customer2.buyTicket('Harry', 60)
customer2.buyTicket('Tomas', 28)
print('6-------------------------')
customer2.showDetails()
