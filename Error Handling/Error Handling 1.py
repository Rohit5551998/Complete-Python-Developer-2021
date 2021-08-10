#Error Handling

while True:
	try:
		age = int(input("Enter a number: "))
		10/age
	except ValueError:
		print("Please enter a number.")
	except ZeroDivisionError:
		print("Please enter age higher than 0.")
	else:
		print("Thank You!")

	