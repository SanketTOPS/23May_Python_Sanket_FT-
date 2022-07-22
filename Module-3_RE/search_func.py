import re

mystr="This is Python!"

x=re.search("is",mystr)

y=re.match("is",mystr)

print(x)
print(y)