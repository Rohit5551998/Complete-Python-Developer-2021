import re

string = 'search this inside of this text please!'

# a = re.search('this', string)
# print(a)
# print(a.span())
# print(a.start())
# print(a.end())
# print(a.group())

pattern = re.compile('this')
a = pattern.search(string)
print(a)

b = pattern.findall(string)
print(b)

pattern1 = re.compile('search this inside of this text please!')
c = pattern1.fullmatch(string)
print(c)

pattern2 = re.compile('search this inside of this text')
d = pattern2.match(string)
print(d)