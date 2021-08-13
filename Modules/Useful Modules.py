from collections import Counter, defaultdict, OrderedDict

li = [1, 2, 3, 4, 5, 6, 7]
sentence = "blah blah blah thinking about python"

print(Counter(li))
print(Counter(sentence))


dictionary = defaultdict(lambda: 'Does not Exist', {'a': 1, 'b': 2})
print(dictionary['a'])

import datetime as dt

print(dt.time(5, 45, 3))
print(dt.date.today())

from array import array

arr = array('i', [1,2 ,3])
print(arr)