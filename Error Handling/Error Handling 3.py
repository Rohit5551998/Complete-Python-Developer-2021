#Error Handling

while True:
	try:
		age = int(input("Enter a number: "))
		10/age
		raise ValueError('Hey cut it out')
	# except ValueError:
	# 	print("Please enter a number.")
	# 	continue
	except ZeroDivisionError:
		print("Please enter age higher than 0.")
		break
	else:
		print("Thank You!")
		break
	finally:
		print("Ok, I am finally done")
	print("Can you hear me?")
	