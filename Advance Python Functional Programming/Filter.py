# Filter

myList = [1, 2, 3]

def check_odd(item):
	return item%2 != 0
	
print(list(filter(check_odd, myList)))

print(list(filter(lambda x: x%2 == 1, myList)))

print(myList)