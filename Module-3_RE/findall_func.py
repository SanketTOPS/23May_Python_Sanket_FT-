import re

mystr=input("Enter any string:")

x=re.findall("is",mystr)

print(x)

if x:
    print("Match Done....")
else:
    print("Error....Try again!")

