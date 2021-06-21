#Exercise: First GUI

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

new_line = []

for row in picture:
	for element in row:
		if element == 0:
			new_line.append(" ")
		elif element == 1:
			new_line.append("*")
	print("".join(new_line))
	new_line = []
