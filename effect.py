class StatusEffect():
   def __init__(self):
        self.attack_multiplier = 1.0
        self.block_multiplier = 1.0
        self.heal_per_turn = 0
        self.damage_per_turn = 0


strengthened = StatusEffect()
strengthened.attack_multiplier = 1.5

weakened = StatusEffect()
weakened.attack_multiplier = 0.75

frail = StatusEffect()
frail.block_multiplier = 0.75