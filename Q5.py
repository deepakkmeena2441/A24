from ast import Delete


class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=0
        self.email=email
    def show(self):
        print(self.name,self.email)
    def Deleteage(self):
        del self.age




a=user("Arpit",0,"harpitjain0207gmail.com")
a.Deleteage()
a.show()

        
    