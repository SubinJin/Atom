class PartyAnimal :
    x = 0
    name = ""
    def __init__(self, nam) :
        self.name = nam
        print(self.name, ' constructed')

    def party(self) :
        self.x = self.x + 1
        print(self.name, ' party conut ', self.x)

class FootballFan(PartyAnimal) : # 상속
    points = 0

    def touchdown(self) :
        self.points = self.points + 7
        self.party()
        print(self.name, ' points ', self.points)

s = PartyAnimal('Sally') # Sally  constructed
s.party() # Sally  party conut  1

j = FootballFan('Jim') # Jim  constructed
j.party() # Jim  party conut  1
j.touchdown()
# Jim  party conut  2
# Jim  points  7
