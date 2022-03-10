class Card:
    def __init__(self, attack = 5, block = 0):
        self.attack = attack
        self.block = block
        self.name = 'Attack'
        self.cost = 1
        self.id = 1
    def __repr__(self):
        return self.name
