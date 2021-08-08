#List Comprehension

mylist = [char for char in 'hello']
# print(mylist)

mylist2 = [num for num in range(0, 100)]
# print(mylist2)

mylist3 = [num**2 for num in range(0, 100)]
# print(mylist3)

mylist4 = [num**2 for num in range(0, 100) if (num%2) == 0]
# print(mylist4)

#Set Comprehension

mylist = {char for char in 'hello'}
# print(mylist)

mylist2 = {num for num in range(0, 100)}
# print(mylist2)

mylist3 = {num**2 for num in range(0, 100)}
# print(mylist3)

mylist4 = {num**2 for num in range(0, 100) if (num%2) == 0}
# print(mylist4)

#Dictionary Comprehension

simple_dict = {
	'a': 1,
	'b': 2
}

my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
# print(my_dict)

my_dict2 = {num:num*2 for num in [1, 2, 3]}
print(my_dict2)