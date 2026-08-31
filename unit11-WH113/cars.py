class Car:
    TANK_SIZE = 15
    MPG = 30

    __slots__ = ['__vin', '__make', '__model', '__year', '__mileage', '__fuel']
        
    def __init__ (self, vin, make, model, year):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = 0
        self.__fuel = 0

    def __repr__ (self):
        return "Car: \n" \
               + " Vin = " + self.__vin + "\n" \
               + " Make = " + self.__make + "\n" \
               + " Model = " + self.__model + "\n" \
               + " Year = " + str (self.__year) + "\n" \
               + " Mileage = " + str (self.__mileage) + "\n" \
               + " Fuel = " + str (self.__fuel)
    
    def __str__ (self):
        return "Car: {VIN = " + self.__vin + ", Make = " + self.__make + ", Model = " +  self.__model + \
           ", Year = " + str (self.__year) + ", Miles = " + str (self.__mileage) + ", Fuel = " + str (self.__fuel) + "}"

    def __eq__ (self, other):
        if type (self) == type (other):
            return self.__vin == other.__vin
        else:
            False

    def __lt__ (self, other):
        if type (self) == type (other):
            return self.__vin < other.__vin
        else:
            False

    def __le__ (self, other):
        if type (self) == type (other):
            return self.__vin <= other.__vin
        else:
            False

    def __gt__ (self, other):
        if type (self) == type (other):
            return self.__vin > other.__vin
        else:
            False

    def __ge__ (self, other):
        if type (self) == type (other):
            return self.__vin >= other.__vin
        else:
            False

    def __hash__ (self):
        return hash (self.__vin)

    def get_vin (self):
        return self.__vin
    
    def get_make (self):
        return self.__make
    
    def get_model (self):
        return self.__model
    
    def get_year (self):
        return self.__year
    
    def get_mileage (self):
        return self.__mileage
    
    def get_fuel (self):
        return self.__fuel
    
    def filler_up (self, gallons):
        self.__fuel += gallons
        if self.__fuel > Car.TANK_SIZE:
            self.__fuel = Car.TANK_SIZE

    def drive (self, miles):
        fuel_used = miles / Car.MPG
        if fuel_used > self.__fuel:
            fuel_used = self.__fuel

        self.__fuel -= fuel_used
        self.__mileage += fuel_used * Car.MPG

def print_car (car):
    print ("Car: {VIN =", car.get_vin (), ", Make =", car.get_make (), ", Model =", car.get_model (),
           ", Year =", car.get_year (), ", Miles =", car.get_mileage (), ", Fuel =", car.get_fuel (), "}")
    
def main ():
    car1 = Car ("123ABC", "Saturn", "SL2", 2000)
    car2 = Car ("234ABC", "Saturn", "Sky Redline", 2007)
    car3 = Car ("123ABC", "Saturn", "SL2", 2000)
    car_list = [car1, car2, car3,
                Car ("567ABC", "Subaru", "Crosstrek", 2015),
                Car ("987ABC", "Subaru", "Soltera", 2023)]


    print_car (car1)
    print_car (car2)

    car1.filler_up (10)
    car2.filler_up (100)
    print_car (car1)
    print_car (car2)    

    car1.drive (150)
    car2.drive (1500)
    print_car (car1)
    print_car (car2)   

    print (str (car1))
    print (car2)

    print (car1 == car2)
    print (car1 == car3)

    car_list.sort ()
    for car in car_list:
        print (car)

    print ()
    
    car_set = set (car_list)
    for car in car_set:
        print (car)

main ()