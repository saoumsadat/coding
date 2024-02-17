# creating class
class Pokemon:
	def __init__(self, pok1n, pok2n, pok1p, pok2p, dr):
		self.pokemon1_name = pok1n
		self.pokemon1_power = pok1p
		self.pokemon2_name = pok2n
		self.pokemon2_power = pok2p
		self.damage_rate = dr

# given code
team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name, team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name, team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power + team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)

# subtask 2
team_bulb = Pokemon('balbasaur', 'squirtle', 80, 70, 9)
# subtask 3
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name, team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name, team_bulb.pokemon2_power)
#bulb_combined_power = (team_bulb.pokemon1_power) #beshi boro line
pok2p1 = team_bulb.pokemon1_power
pok2p2 = team_bulb.pokemon2_power
dr = team_bulb.damage_rate
bulb_p = (pok2p1 + pok2p2) * dr
print('Combined Power:', bulb_p)