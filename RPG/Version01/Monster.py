from random import randint

import Monster


class Noob:
    def __init__(self):
        self.strength = 1
        self.dexterity = 1
        self.intelligence = 1
        self.damage = self.strength * 2
        self.luck = randint(0, 1)
        self.life = 10
        self.max_life = 10
        self.defence = 1
        self.magic_defence = int((self.intelligence / 3) + self.defence)
        self.xp = int((self.strength + (self.defence / 2))) * 2

    def easy(self):
        self.strength += 2
        self.damage = self.strength * 3
        self.life *= 1
        self.max_life *= 1
        self.defence += 2

    def medium(self):
        self.strength += 4
        self.damage = self.strength * 2
        self.life *= 1.5
        self.max_life *= 1.5
        self.xp *= 1.1
        self.defence += 3

    def hard(self):
        self.strength += 6
        self.damage = self.strength * 2
        self.life *= 2
        self.max_life *= 2
        self.xp *= 1.3
        self.luck += 3
        self.defence += 4

    def print_monster_stats(self):
        print(f"\n======== Monster Stats ========"
              f"\n            Life: {int(self.life)}"
              f"\n          Strength: {self.strength}"
              f"\n           Damage: {int(self.damage)}"
              f"\n          Defence: {self.defence}"
              f"\n       Magic Defence: {self.magic_defence}")
        return '======================='


def combat_difficult(level):
    difficult = randint(0, 5)
    if level == 'Noob':
        if difficult <= 2:
            monster = Monster.Noob()
            monster.easy()
            print('Easy combat!')
            return monster
        elif difficult > 2 < 4:
            monster = Monster.Noob()
            monster.medium()
            print('Medium combat!')
            return monster
        else:
            monster = Monster.Noob
            monster.hard()
            print('Hard combat!')
            return monster
