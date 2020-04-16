from vehicle import Vehicle

# Electric motorcycle
class Zero:
    def __init__(self):
        self.battery_kwh = 0
        self.main_color = ""
        self.maximum_occupancy = 0

    def charge_battery(self):
        pass

# Propellor light aircraft
class Cessna:
    def __init__(self):
        self.fuel_capacity = 0
        self.main_color = ""
        self.maximum_occupancy = 0

    def refuel_tank(self):
        pass

# Electric car
class Tesla(Vehicle):
    def __init__(self, color, kwh):
        super().__init__(color)
        self.battery_kwh = kwh
        # self.main_color = ""
        # self.maximum_occupancy = 0

    def charge_battery(self):
        pass

    def drive(self):
        print('The tesla drives itself')

# Gas powered truck
class Ram:
    def __init__(self):
        self.fuel_capacity = 0
        self.main_color = ""
        self.maximum_occupancy = 0

    def refuel_tank(self):
        pass

#---------------------------------------

# my_tesla = Tesla("blue", 30)

# print(my_tesla.battery_kwh)

# my_tesla.drive()

# print(my_tesla.main_color)