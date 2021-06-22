#Class and Static Methods

class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('run')
		return 'done'

	@classmethod
	def adding_things(cls, num1, num2):
		return cls("Teddy", num1 + num2)

	@staticmethod
	def adding_things2(num1, num2):
		return num1 + num2

player3 = PlayerCharacter.adding_things(5,6)
print(player3.age)
print(PlayerCharacter.adding_things2(11, 10))