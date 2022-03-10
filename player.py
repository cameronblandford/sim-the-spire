from card import Card
import random

attack_card = Card()
attack_card.attack = 6
attack_card.block = 0
attack_card.name = 'Strike'

block_card = Card()
block_card.attack = 0
block_card.block = 5
block_card.name = 'Defend'

class Player:
    def __init__(self):
        self.deck = [attack_card, attack_card, attack_card, attack_card, attack_card, block_card, block_card, block_card, block_card, block_card, attack_card, block_card]
        self.drawpile = self.deck
        random.shuffle(self.drawpile)
        self.hand = []
        self.draw_n(5)
        self.discardpile = []
        self.hp = 100
        self.block = 0
        self.name = 'Clam'
        self.energy = 3
        self.max_energy = 3

    def discard(self, card):
        self.hand.remove(card)
        self.discardpile.append(card)

    def check_reshuffle(self):
        if not self.drawpile:
            print('drawpile empty, reshuffling')
            self.drawpile = self.discardpile.copy()
            random.shuffle(self.drawpile)
            self.discardpile = []

    def draw(self):
        self.check_reshuffle()
        drawn_card = self.drawpile.pop()
        self.hand = self.hand + [drawn_card]
        print('drew a new card: %s' % drawn_card)
        self.check_reshuffle()

    def draw_n(self, n):
        for _ in range(0, n):
            self.draw()

    def clear_hand(self):
        self.discardpile = self.discardpile + self.hand.copy()
        self.hand = []

    def play(self, card, target):
        if (self.energy < card.cost):
            print('NOT ENOUGH ENERGY')
            return
        self.energy -= card.cost
        self.block += card.block
        difference = target.block - card.attack
        if difference < 0:
            target.block = 0
            target.hp += difference
        else:
            target.block -= card.attack
        print('%s plays %s card!' % (self.name, card.name))
        # print('%s takes %s damage (%s hp left)!' % (target.name, card.attack, target.hp))
        # print('%s gains %s block (%s block total)!' % (self.name, card.block, self.block))
        self.discard(card)

    def __repr__(self):
        return "%s: (%s hp) (%s block)" % (self.name, self.hp, self.block)
