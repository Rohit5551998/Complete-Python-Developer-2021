#Error Handling

def sum(num1, num2):
	try:
		return num1/num2
	except (TypeError, ZeroDivisionError) as err:
		print(f"Oops!: {err}")

print(sum(2, '1'))