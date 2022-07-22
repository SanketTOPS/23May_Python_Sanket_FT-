class nirav:
    nid=0
    nbranch=""

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nbranch=input("Enter Nirav's Branch:")

class darshan:
    did=0
    dbranch=""

    def d_getdata(self):
        self.did=input("Enter Darshan's ID:")
        self.dbranch=input("Enter Darshn's Branch:")

class gopal:
    gid=0
    gbranch=""

    def g_getdata(self):
        self.gid=input("Enter Gopal's ID:")
        self.gbranch=input("Enter Gopal's Branch:")

class college(nirav,darshan,gopal): #multiple inher.
    def printdata(self):
        print("-------Nirav Data------\n")
        print("Nirav's ID:",self.nid)
        print("Nirav's Branch:",self.nbranch)
        print("-------Darshan Data------\n")
        print("Darshan's ID:",self.did)
        print("Darshan's Branch:",self.dbranch)
        print("-------Gopal Data------\n")
        print("Gopal's ID:",self.gid)
        print("Gopal's Branch:",self.gbranch)


cl=college()
cl.n_getdata()
cl.d_getdata()
cl.g_getdata()
cl.printdata()