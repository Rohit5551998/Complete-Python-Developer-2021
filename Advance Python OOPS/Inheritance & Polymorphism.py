class User():
	def sign_in(self):
		print('Logged In')

class Wizard(User):
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		print(f'Attacking with power of {self.power}')

class Archer(User):
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows

	def attack(self):
		print(f'Attacking with arrows: arrows left- {self.num_arrows}')

wiz1 = Wizard("Adam", 50)
arch1 = Archer("Robin", 500)

def player_attack(char):
	char.attack()

player_attack(wiz1)
player_attack(arch1)