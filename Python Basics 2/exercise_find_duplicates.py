#Exercise: Finding Duplicates

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

some_dict = {}
duplicates = []

for i in some_list:
	if i not in some_dict:
		some_dict[i] = 1
	else:
		duplicates.append(i)

print(duplicates)

#Without Dictionaries
duplicates = []

for value in some_list:
	if some_list.count(value) > 1:
		if value not in duplicates:
			duplicates.append(value)
print(duplicates)
	