class student:
    __stid=12
    __stnm="Mitesh"

    def getdata(self):
        print("This is getdata function.")
    
    def stdata(self):
        print("Student ID:",self.__stid)
        print("Student Name:",self.__stnm)
    
    def __getsum(self,a,b):
        print("Sum:",a+b)

    def answer(self):
        self.__getsum(34,65)

st=student()
#print("ID:",st.stid)
#print("Name:",st.stnm)
st.getdata()
st.stdata()
st.answer()
