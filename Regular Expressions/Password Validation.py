import re

pattern = re.compile(r"[a-zA-Z0-9$%#@]{7,}[0-9]")

password = "dfghythgsdjhdwoadjiwajd13232$#@51"
pass1= "1221"
a = pattern.fullmatch(password)
print(a)