mydict={'id':101,'name':'nirav','sub':'python'}

#print(mydict)
#print(mydict.get('name'))
#print(mydict['sub'])

#mydict["id"]=102
#print(mydict)

"""for i in mydict:
    print(i)"""

"""for i in mydict.values():
    print(i)"""

"""for i in mydict.items():
    print(i)"""

# Key=id and Value=101
# Key=name and Value=nirav
# Key=sub and Value=python

"""for i,j in mydict.items():
    print(f"Key={i} and Value={j}")"""

print(mydict)
#print(mydict.keys())
#print(mydict.values())

#mydict["city"]="Rajkot"
#print(mydict)

"""if 'hitesh' in mydict.values():
    print("Yes...")
else:
    print("Noo")"""


#print(len(mydict))

#mydict.pop('name')
#del mydict['sub']
#del mydict
#print(mydict)


newdict=mydict.copy()
print(newdict)