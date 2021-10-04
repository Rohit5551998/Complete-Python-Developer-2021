with open('hello.txt') as my_file:
	print(my_file.readlines())

# Clear file and write
# with open('hello.txt', 'w') as my_file:
# 	text = my_file.write(':)')
# 	print(text)

# Overwrite existing characters
# with open('hello.txt', 'r+') as my_file:
# 	text = my_file.write(':)')
# 	print(text)

with open('hello.txt', 'a') as my_file:
	text = my_file.write(':)')
	print(text)