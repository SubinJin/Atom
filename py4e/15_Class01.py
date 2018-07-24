class PartyAnimal :
    x = 0

    def party(self) :
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()
an.party() # 1
an.party() # 2
an.party() # 3
PartyAnimal.party(an) # 4
PartyAnimal.party(PartyAnimal()) # 1
PartyAnimal.party(PartyAnimal()) # 1
# an이 아니기 때문에 처음부터 시작함
# PartyAnimal()을 집어 넣으면 계속 처음부터?
# an = PartyAnimal()인데 왜 결과가 다를까?
