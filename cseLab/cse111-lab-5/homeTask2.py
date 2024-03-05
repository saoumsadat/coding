menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}

#code
class Foodie:
	def __init__(self, name):
		self.name = name
		self.all_items = []
		self.spent = 0

	def show_orders(self):
		s = f"{self.name} has {len(self.all_items)} item(s) in the cart."
		s += f"\nitems: {self.all_items}"
		s += f"\nTotal spent: {self.spent}."
		return s
	
	def order(self, *items):
		for item in items:
			item_name = item.split('-')[0]
			item_quantity = int(item.split('-')[1])
			item_price = menu[item_name]
			total_price = item_price * item_quantity

			print(f"Ordered - {item_name}, quantity - {item_quantity}, price (per Unit) - {item_price}.")
			print(f"Total Price - {total_price}")

			self.all_items.append(item_name)
			self.spent += total_price
	
	def pay_tips(self, m = 0):
		if (m): 
			print(f"Gives {m}/- tips to waiter.")
			self.spent += m
		else: print("No tips to the waiter.")

f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())