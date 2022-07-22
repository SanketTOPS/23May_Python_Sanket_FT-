techlist=['C','C++','JAVA','Python','.NET']

#print(techlist)

#print(techlist[0])
#print(techlist[2])
#print(techlist[-1])
#print(techlist[0:3])
#print(techlist[2:])
#print(techlist[:3])

#print(techlist)
#techlist[2]='Android' # update
#print(techlist)

#print(techlist)


"""for i in techlist:
    print(i)
"""

#print(techlist.index('Python'))

# Index[0] = C
# Index[1] = C++
# Index[2] = JAVA

"""for i in techlist:
    #print(i)
    print(f"Index[{techlist.index(i)}] = {i}")"""

"""n=0
for i in techlist:
    print(f"Index[{n}] = {i}")
    n+=1"""


"""if "C#" in techlist:
    print("Yes....")
else:
    print("Noo")"""



techlist.append("Android")
techlist.insert(3,'React')
#techlist.remove("C++")
#techlist.pop()
#techlist.pop(2)
#techlist.clear()

#del techlist[2]
#del techlist
#print(techlist)

#newlist=techlist.copy()
#print(newlist)


#newlist=["Node","Angular","React","Perl"]

#print(techlist+newlist)
#techlist.extend(newlist)
#print(techlist)

print(techlist)
#techlist.reverse()
techlist.sort()
print(techlist)