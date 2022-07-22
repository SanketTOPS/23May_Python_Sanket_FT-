main_list=[]

sub=[]

n=int(input("Enter Number of elements for subject:"))

for i in range(n):
    s_el=input("Enter Subject:")
    sub.append(s_el)

fnm=[]

x=int(input("Enter Number of elements for faculty:"))

for j in range(x):
    f_el=input("Enter Faculty Name:")
    fnm.append(f_el)

main_list.append(sub)
main_list.append(fnm)
print(main_list)