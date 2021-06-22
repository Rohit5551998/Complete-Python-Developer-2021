#Scope Variables
total = 0


def count():
	global total
	total += 1
	return total

count()
count()
print(count())

def count1(total):
	total += 1
	return total

print(count1(count1(count1(total))))
#1 - Start with local
#2 - Parent local?
#3 - Global
#4 - Built-In Python Functions.