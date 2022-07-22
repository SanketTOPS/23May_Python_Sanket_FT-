myset={'A','B','C','D','E','F'}

print(myset)
#print(myset[0])

"""if 'B' in myset:
    print("Yes...")
else:
    print("No...")"""

"""for i in myset:
    print(i)"""

#myset.add("G")
#myset.update(["H","I","J","A","B","C"])
#myset.remove("F")
#myset.pop()
#print(myset)

# ----------------------------- #

newset={"P","Q","R","S","A","C","D"}
#print(newset)

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)