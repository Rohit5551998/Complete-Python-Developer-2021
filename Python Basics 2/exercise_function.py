#Exercise: Functions
def highest_even(l1):
	max = -1
	for i in l1:
		if i%2 == 0 and i>max:
			max = i
	return max
print(highest_even([10, 2, 4, 6, 8, 11]))