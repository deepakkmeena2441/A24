class user:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
    def show(self):
        print(self.name,self.age,self.email)

a=user("arpit",20,"harpitjain0207@gmail.com")
b=user("Anup",18,"anupjain0203@gmail.com")
a.show()
b.show()

        
    