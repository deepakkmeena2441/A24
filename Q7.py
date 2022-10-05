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
comp1=laptop("hp","i7",16,1000)
comp1.config()
