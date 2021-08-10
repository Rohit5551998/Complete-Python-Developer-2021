#Square
myList = [5, 4, 3]
print(list(map(lambda x: x**2, myList)))

#List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda x:x[1]))
print(a)
# a.sort(key=lambda x: x[1])
# print(a)