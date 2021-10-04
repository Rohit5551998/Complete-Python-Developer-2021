import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

email = 'abc@xyz.com'

a = pattern.match(email)
print(a.group())