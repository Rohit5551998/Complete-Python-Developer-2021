# Map

print(list(map(lambda x:x*2, [5, 10, 20, 40])))

my_list=[1, 2, 3]

def multiply_by_2(item):
	return item*2

print(list(map(multiply_by_2, my_list)))
print(my_list)