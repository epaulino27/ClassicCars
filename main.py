class Vehicle: #make class Vehicles
    def __init__(self,make,model,year,weight): #assign attributes
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def display_info(self):#print out vehicles details neatly
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Weight: {self.weight}")
        return

    def honk(self):#print a honk sound
        print("Beep!Beep!")

    @staticmethod
    def is_motorcycle(weight):#check if weight is below 500kg
        if weight < 500:
            return True
        else:
            return False


# Assuming the Vehicle class is defined in a file named 'vehicle.py'


# Test driver code
if __name__ == "__main__":
    # Create instances of Vehicle
    car = Vehicle("Toyota", "Corolla", 2021, 1275.0)
    motorcycle = Vehicle("Harley-Davidson", "Street 750", 2019, 220.0)

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print("Is the car a motorcycle?", Vehicle.is_motorcycle(car.weight))
    print()

    # Display information of the motorcycle
    print("Motorcycle Info:")
    motorcycle.display_info()
    motorcycle.honk()
    print("Is the motorcycle actually a motorcycle?", Vehicle.is_motorcycle(motorcycle.weight))
    print()

    # Show total number of vehicles created, if you are going for the Bonus
    print(f"Total number of vehicles: {Vehicle.number_of_vehicles}")