import datetime as date


class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def printVehicleDetails(self):
        msg="Vehicle make is {} and model is {} , year of manufacture is {}"
        print(msg.format(self.make,self.model,self.year))

class Car(Vehicle):
    def __init__(self,make,model,year,vehicleType):
         super().__init__(make,model,year)
         self.vehicleType=vehicleType

    def printCarDetails(self):
        msg="The vehicle type is \'{}\' and make is \'{}\' and model is \'{}\' with manufacture year \'{}\'"
        print(msg.format(self.vehicleType,self.make,self.model,self.year))
        
def welcomeMessage():
    msg = "Welcome to the \"Vehicle\" module!!!\nDay: {}"
    dateVal= date.datetime.now()
    print(msg.format(dateVal.strftime("%c")))
