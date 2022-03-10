import time
from engine import Intent, Player, Enemy, Card
from numpy import random
p = Player()
e = Enemy()

def sort_key_func(card):
    return card.block


def chooseCards(player, enemy):
    player.hand.sort(key=sort_key_func, reverse=True)
    print('---player turn---')
    for card in player.hand:
        print('---looking at %s card---' % card.name)
        # play it if it has block and the we need more block
        if enemy.current_intent.attack > player.block and player.energy >= card.cost and card.block > 0:
            player.play(card, e)
        # if we dont need it, we should attack the enemy
        if card.attack > 0:
            player.play(card, e)

class Floor():
    def __init__(self, player = p, enemy = e):
        self.player = player
        self.enemy = enemy
    def run_sim(self, callback):
        turn = 1
        while self.player.hp > 0 and self.enemy.hp > 0:
            self.player.block = 0
            self.player.clear_hand()
            self.player.draw_n(5)
            self.player.energy = self.player.max_energy
            print('--------------------------------------')
            print('TURN %s' % turn)
            print('drawpile: %s' % self.player.drawpile)
            print('hand: %s' % self.player.hand)
            print('discardpile: %s' % self.player.discardpile)
            print('---player and enemy status---')
            print(self.player)
            print(self.enemy)
            # enemy chooses an intent
            self.enemy.current_intent = random.choice(self.enemy.intents)
            if (self.enemy.current_intent.block):
                print('%s prepares to block for %s!' % (self.enemy.name, self.enemy.current_intent.block))            
            if (self.enemy.current_intent.attack):
                print('%s prepares to attack for %s!' % (self.enemy.name, self.enemy.current_intent.attack))
            # player plays cards
                # for each card
            callback(self.player, self.enemy)
            # enemy moves
            print('---enemy turn---')
            self.enemy.block = 0
            self.enemy.move(p)
            turn += 1
            time.sleep(1)
        print('---FINISHED---')
        print(self.player)
        print(self.enemy)

f = Floor()
f.run_sim(chooseCards)