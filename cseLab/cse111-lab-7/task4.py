class Spaceship:
    def __init__(self, name, cap):
        self.__name = name
        self.__capacity = cap
        self.curr_weight = 0
        self.cargoList = []
    
    def load_cargo(self, cargo):
        total = self.curr_weight + cargo.getWeight()
        if (total > self.__capacity):
            print(f"Warning: Unable to load {cargo.getName()} inside {self.__name}. Exceeds capacity by {total - self.__capacity}.")
            return
        self.curr_weight += cargo.getWeight()
        self.cargoList.append(cargo.getName())

    def display_details(self):
        print("Spaceship Name: ", self.__name)
        print("Capacity: ", self.__capacity)
        print("Current Cargo Weight: ", self.curr_weight)
        print("Cargo: ", self.cargoList)


class Cargo:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    
    def getName(self):
        return self.__name
    def getWeight(self):
        return self.__weight

# Creating spaceships
falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
# Creating cargo
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")
# Loading cargo onto spaceships
falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)  # Apollo will not reach its total capacity
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)  # This should exceed Falcon's capacity
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)  # This should not exceed Enterprise's capacity
enterprise.display_details()
