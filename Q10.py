class employee:
    def __init__(self):
       self.empid=0
       self.name=""
       self.salary=0
    def inputmethod(self,emplid,name,salary):
        self.empid=emplid
        self.name=name
        self.salary=salary
    def display(self):
        print(self.name)
        print(self.empid)
        print(self.salary)




a=employee()
a.inputmethod(2034,"daksh",70000)
a.display()





