#counter & range & enumerate

my_list = [i for i in range(1, 11)]
sum = 0
for i in my_list:
	sum += i

print(sum)

for i,char in enumerate(list(range(100))):
	if char == 50:
		print(f'{char}\'s index is {i}')