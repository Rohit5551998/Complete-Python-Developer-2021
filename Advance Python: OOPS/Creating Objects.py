#OOPS

class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('run')
		return 'done'

p1 = PlayerCharacter("Virat", 44)
p2 = PlayerCharacter("Kane", 43)
print(p1.name)
print(p1.run())
print(p2.name)
p2.attack = 50
print(p2.attack)