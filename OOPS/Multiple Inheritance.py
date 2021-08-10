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

	def check_arrows(self):
		print(f'Attacking with arrows: arrows left- {self.num_arrows}')

	def run(self):
		print('Ran really fast')

class HybridBorg(Wizard, Archer):
	def __init__(self, name, power, arrows):
		Wizard.__init__(self, name, power)
		Archer.__init__(self, name, arrows)

hb1 = HybridBorg('Adam', 50, 100)
print(hb1.sign_in())
print(hb1.attack())
print(hb1.check_arrows())
