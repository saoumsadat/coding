class BracuStudent:
    def __init__(self, name, home):
        self.name = name
        self.home = home
        self.busPass = False

    def show_details(self):
        print("Student Name: ", self.name)
        print("Lives in", self.home)
        print("Have Bus Pass? ", self.busPass)

    def get_pass(self):
        if (self.busPass):
            print("You already have Bus Pass")
            return
        self.busPass = True

class BracuBus:
    def __init__(self, route, maxPass = 2):
        self.route = route
        self.maxPass = maxPass
        self.passList = []
    
    def show_details(self):
        print("Bus Route: ", self.route)
        print(f"Passengers Count: {len(self.passList)} (Max: {self.maxPass})")
        print("Passengers on Board: ", self.passList)
    
    def board(self, *stList):
        if (not(len(stList))):
            print("No passengers!")
            return
        # print(stList)
        for st in stList:
            if (st.home != self.route):
                print("You got on the wrong bus!")
                continue
            elif (st.busPass == False):
                print("You don't have a bus pass!")
                # print(stList)
                continue
            elif (len(self.passList) == self.maxPass):
                print("Bus is full!")
                continue
            self.passList.append(st.name)
            print(f"{st.name} boarded the bus.")


st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
