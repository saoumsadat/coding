class Team:
    def __init__(self, name = ""):
        self.__name = name
        self.__playerList = []
    
    def setName(self, name):
        self.__name = name
    
    def addPlayer(self, *players):
        for player in players:
            self.__playerList.append(player.name)
    
    def printDetail(self):
        print("=" * 21)
        print("Team:", self.__name)
        print(f"List of Players:\n{self.__playerList}")
        print("=" * 21)

class Player:
    def __init__(self, name):
        self.name = name

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
