from player import Player
from enemy import Enemy
from floor import FightFloor

def sort_key_func(card):
    return card.block

def chooseCards(player, enemy):
    player.hand.sort(key=sort_key_func, reverse=True)
    print('---player turn---')
    for card in player.hand:
        print('---looking at %s card---' % card.name)
        # play it if it has block and the we need more block
        if enemy.current_intent.attack > player.block and player.energy >= card.cost and card.block > 0:
            player.play(card, enemy)
        # if we dont need it, we should attack the enemy
        if card.attack > 0:
            player.play(card, enemy)

p = Player()
e = Enemy()
e2 = Enemy()
f = FightFloor(None, p, e)
f.run_sim(chooseCards)
f2 = FightFloor(f, p, e2)
f2.run_sim(chooseCards)