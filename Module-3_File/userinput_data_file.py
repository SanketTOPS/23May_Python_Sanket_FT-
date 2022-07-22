fl=open('stdata.txt','a')

id=input("Enter your ID:")
name=input("Enter your Name:")
sub=input("Enter your Subject:")

fl.write(f"Student ID:{id}")
fl.write(f"\nStudent Name:{name}")
fl.write(f"\nStudent Subject:{sub}")
