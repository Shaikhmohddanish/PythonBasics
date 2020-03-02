class car:
    def __init__(self,company_name):
        self.company_name="Hyundai"
    def info(self):
        print("Hyundai")
class sportscar(car):
    def info1(self):
        print("Lamborghini")
class rentcar(sportscar,car):
    def info2(self):
        print("Getz")
obj1=rentcar("abc")
obj1.info()
obj1.info1()
obj1.info2()