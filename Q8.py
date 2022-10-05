
class laptop:
    def __init__(self,brand,cpu,ram,hdd):
        self.brand=brand
        self.cpu=cpu
        self.ram=ram
        self.hdd=hdd
    def config(self):
        print(self.brand)
        print(self.cpu)
        print(self.ram)
        print(self.hdd)

l=[]
comp1=laptop("hp","i7","32gb","512gb")
comp2=laptop("asus","i7","8gb","512gb")
comp3=laptop("dell","i9","32gb","250gb")
#comp1.config()
l.append(comp1)
l.append(comp2)
l.append(comp3)
l.sort(reverse=True,key=lambda x:x.ram)
for e in l:
    print(" {} {} {} {}".format(e.brand,e.cpu,e.ram,e.hdd))




    


