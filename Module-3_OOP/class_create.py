class student:
    stid=12
    stnm='Nirav'

    def myfunc(self):
        print("This is student class.")


# Object

"""st=student()
print("Student ID:",st.stid)
print("Student Name:",st.stnm)
#st.myfunc()
st.stid=67
st.stnm="Mitesh"
print("Student ID:",st.stid)
print("Student Name:",st.stnm)
"""

# Instance
print("Student ID:",student().stid)
print("Student Name:",student().stnm)
student().stid=34
student().stnm="Sanket"
print("Student ID:",student().stid)
print("Student Name:",student().stnm)

