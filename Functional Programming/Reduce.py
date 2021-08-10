# Reduce
from functools import reduce

myList = [1, 2, 3]

def accumulator(acc, item):
	return (acc - item)

print(reduce(accumulator, myList, 10))
print(reduce(lambda x,y: x-y, myList, 10))
print(myList)