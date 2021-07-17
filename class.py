class Car(object):
    def __init__(self,model,color,company,speedlimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedlimit = speedlimit

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stoped")

    def accelarate(self):
        print("accelarating...")

    def changegear(self,gear_type):
        print("gear changed")

audi = Car("a6","black","audi",90)
print(audi.start())