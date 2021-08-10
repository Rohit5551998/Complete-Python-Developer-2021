#Decorator

def my_decorator(func):
	def wrapper_func(*args, **kwargs):
		print('**********')
		func(*args, **kwargs)
		print('**********')
	return wrapper_func

@my_decorator
def hello(greeting, emoji=':('):
	print(greeting, emoji)

hello('hiiiiii')