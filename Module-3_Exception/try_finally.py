try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print("Sum:",a+b)
except Exception as e:
    print(e)
else:
    fnm=input("Enter Firstname:")
    lnm=input("Enter Lirstname:")
    print("Fullname:",fnm+" "+lnm)