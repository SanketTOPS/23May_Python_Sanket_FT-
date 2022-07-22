class homepage:
    def login(self,username,password):
        print("Username:",username)
        print("Password:",password)

class mobilepage(homepage):
    def login(self, username, password):
        return super().login(username, password)

mb=mobilepage()
mb.login("sanket2020","Tops?123")