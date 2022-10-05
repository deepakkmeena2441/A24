class user:
    def __init__(self,age):
        self.age=age
    def compare(self,b,c):
        if self.age>b.age:
            if self.age>c.age:
            
               print("a is youngest")
            else:
                print("c is youngest")


        else:
            if b.age>self.age:
                if b.age>c.age:
                    print("b is youngest")
                else:
                    print("c is youngest")
            





a=user(12)
b=user(23)
c=user(34)
a.compare(b,c)