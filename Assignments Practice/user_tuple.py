mylist=[]

n=int(input("Enter N:"))

for i in range(n):
    el=input("Enter list elem:")
    mylist.append(el)

print(tuple(mylist))