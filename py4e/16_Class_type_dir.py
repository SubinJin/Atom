class PartyAnimal :
    x = 0

    def party(self) :
        self.x = self.x + 1
        print('So Far ', slef.x)

an = PartyAnimal()
print('Type : ', type(an)) # main
print('Dir : ', dir(an)) # 가능한 method 다 보여줌
print('Type : ', type(an.x)) # int
print('Type : ', type(an.party)) # method
