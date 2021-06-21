#List Methods 1

basket = [1,2,3,4,5]
print(len(basket))

basket.append(100)
#Wrong new_list = basket.append(100)
new_list = basket

print(basket) #In-place changes
print(new_list)

basket.insert(4, 200)
print(basket)

basket.extend([50, 75])
print(basket)

basket.pop()
new = basket.pop(0)
print(basket, new)

basket.remove(4)
print(basket)

basket.clear()
print(basket)