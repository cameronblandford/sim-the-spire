class Intent:
    def __init__(self):
        self.attack = 0
        self.block = 0
        self.name = 'attack'

attack_intent = Intent()
attack_intent.attack = 8

block_intent = Intent()
block_intent.block = 8
block_intent.name = 'defend'

class Enemy:
    def __init__(self):
        self.name = 'Slime'
        self.hp = 20
        self.block = 0
        self.intents = [attack_intent, block_intent]
        self.current_intent = None

    def __repr__(self):
        return "%s: (%s hp) (%s block)" % (self.name, self.hp, self.block)

    def move(self, p):
        self.block += self.current_intent.block
        p.block -= self.current_intent.attack
        difference = p.block - self.current_intent.attack
        if difference < 0:
            p.block = 0
            p.hp += difference
        else:
            p.block -= self.current_intent.attack
        # print('%s takes %s damage!' % (p.name, self.current_intent.attack))
        # print('%s gains %s block!' % (self.name, self.current_intent.block))
