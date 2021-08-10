def fibo(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a
		a = b
		b = temp + b

for x in fibo(10000):
	print(x)

def fibo2(number):
	a = 0
	b = 1
	result = []
	for i in range(number):
		result.append(a)
		temp = a
		a = b
		b = temp + b
	return result

# print(fibo2(10000))