class User():
	def __init__(self, email):
		self.email = email

	def sign_in(self):
		print('Logged In')

class Wizard(User):
	def __init__(self, name, power, email):
		#User.__init__(self, email)
		# OR
		super().__init__(email)
		self.name = name
		self.power = power

	def attack(self):
		print(f'Attacking with power of {self.power}')

wiz1 = Wizard('Adam', 50, 'adam@gmail.com')
print(wiz1.email)