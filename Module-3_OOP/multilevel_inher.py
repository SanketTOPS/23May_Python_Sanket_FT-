class gfather:
    gold=0
    house=0

    def g_getdata(self):
        self.gold=input("Enter Gold details:")
        self.house=input("Enter House's details:")

class father(gfather):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter car's details:")
        self.bal=input("Enter bank balance details:")

class son(father):
    def printdata(self):
        print("------Grand Father Details------")
        print("Gold:",self.gold)
        print("House:",self.house)
        print("------Father Details------")
        print("Car:",self.car)
        print("Bank Balance:",self.bal)

sn=son()
sn.g_getdata()
sn.f_getdata()
sn.printdata()


