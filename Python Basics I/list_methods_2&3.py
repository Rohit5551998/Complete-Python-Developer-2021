#List Methods 2 & 3

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

print(basket.index('d'))
print(basket.index('c', 0, 4))
print('x' in basket)
print(basket.count('d'))

basket.sort()
print(basket)

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'f']
print(sorted(basket))

basket.reverse()
print(basket)

splitter = "!"
sentence = splitter.join(["hi", "my", "name", "is", "JOJO"])
print(sentence)

