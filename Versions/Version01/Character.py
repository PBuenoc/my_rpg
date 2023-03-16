from random import randint

import Character

list_race = ['h', 'H', 'e', 'E', 'd', 'D', 'v', 'V']
list_role = ['w', 'W', 'm', 'M', 'a', 'A', 'v', 'V']


class Player:
    def __int__(self):
        self.name = ''
        self.race = ''
        self.classe = ''
        self.life = 20
        self.max_life = 20
        self.strength = 0
        self.defence = 0
        self.dexterity = 0
        self.intelligence = 0
        self.magic = 0
        self.luck = int(randint(0, 3))
        self.xp = 0

    def print_stats(self):
        print(f"\nName: {self.name}"
              f"\nClass: {self.classe}"
              f"\n======== Stats ========"
              f"\n         Life: {self.life}"
              f"\n       Strength: {self.strength}"
              f"\n    Intelligence: {self.intelligence}"
              f"\n       Defence: {self.defence}"
              f"\n      Dexterity: {self.dexterity}"
              f"\n        Magic: {self.magic}")
        return '======================='

    def punch_attack(self):
        dano = round(self.strength * 2)
        if self.dexterity >= 3 and self.strength > 5:
            print(f'Acertou!!'
                  f'\nSoco forte')
            return dano
        elif 0 < self.dexterity <= 4 <= self.strength:
            print(f'Acertou!!'
                  f'\nSoco fraco')
            return int(dano * 0.4)
        else:
            return "Errou!"

    def spell_attack(self):
        dano = self.magic * 1.5
        if self.intelligence >= 6 and self.magic >= 5:
            print(f'Consiguiu!!'
                  f'\nFeitiço forte')
            return dano
        elif 6 <= self.intelligence and self.magic >= 3:
            print(f'Conseguiu!!'
                  f'\nFeitiço fraco')
            return int(dano * 0.6)
        else:
            return "Você não pode lançar o feitiço!"

    def arrow_attack(self):
        dano = self.dexterity * 2
        if self.luck == 2 or 3:
            if self.intelligence >= 7 and self.dexterity >= 6:
                print(f'Acertou!!'
                      f'\nFlecha certeira!!')
                return dano
            elif 5 <= self.intelligence and self.dexterity >= 6:
                print('Flecha pegou de raspão')
                return int(dano / 2)
            else:
                print('Errou')
                return dano == 0
        else:
            print("Errou! Você está sem sorte!")
            return dano == 0


class Human(Character.Player):
    def __init__(self, name):
        self.name = name
        self.race = 'Human'
        self.classe = ''
        self.life = 20
        self.max_life = 20
        self.strength = 5
        self.defence = 2
        self.dexterity = 3
        self.intelligence = 4
        self.magic = 0
        self.luck = int(randint(0, 3))
        self.xp = 0


class Elf(Character.Player):
    def __init__(self, name):
        self.name = name
        self.race = 'Elf'
        self.classe = ''
        self.life = 20
        self.max_life = 20
        self.strength = 1
        self.defence = 2
        self.dexterity = 4
        self.intelligence = 5
        self.magic = 2
        self.luck = int(randint(0, 3))
        self.xp = 0


class Dwarf(Character.Player):
    def __init__(self, name):
        self.name = name
        self.race = 'Dwarf'
        self.classe = ''
        self.life = 20
        self.max_life = 20
        self.strength = 5
        self.defence = 4
        self.dexterity = 3
        self.intelligence = 2
        self.magic = 0
        self.luck = int(randint(0, 3))
        self.xp = 0


def race_start():
    line = '=============='
    character = None
    choice = 'nada'
    print('======= Olá Jogador! =======')
    name = input('Me informe seu nome: ')
    print()
    while choice not in list_race[0:6]:
        choice = str(input('Qual será sua raça?'
                           '\nHumano [h,H]'
                           '\nElfo [e,E]'
                           '\nAnão [d,D]'
                           '\nVer specs de cada raça [v/V]'
                           '\n>'))
        if choice in list_race[0:2]:
            character = Human(name)
        elif choice in list_race[2:4]:
            character = Elf(name)
        elif choice in list_race[4:6]:
            character = Dwarf(name)
        elif choice in list_race[6:8]:
            print(f'{line}')
            print('Human Stats:'
                  f'\nLife = 20'
                  '\nStrength = 5'
                  '\nDefence = 2'
                  '\nDexterity = 3'
                  '\nIntelligence = 4'
                  '\nMagic = 0')
            print(f'{line}')
            input('\nType any key to continue... >')
            print(f'\n{line}')
            print('Elf Stats:'
                  f'\nLife = 20'
                  '\nStrength = 1'
                  '\nDefence = 2'
                  '\nDexterity = 4'
                  '\nIntelligence = 5'
                  '\nMagic = 2')
            print(f'{line}')
            input('\nType any key to continue... >')
            print(f'\n{line}')
            print('Dwarf Stats:'
                  f'\nLife = 20'
                  '\nStrength = 5'
                  '\nDefence = 4'
                  '\nDexterity = 3'
                  '\nIntelligence = 2'
                  '\nMagic = 0')
            print(f'{line}\n')
    return character


def classDefinition(character):
    classChoice = 'nada'
    line = '=============='
    while classChoice not in list_role[0:6]:
        classChoice = input('Informe sua classe:'
                            '\nWarrior [w, W]'
                            '\nMage [m, M]'
                            '\nArcher [a, A]'
                            '\nVer specs de cada classe [v, V]'
                            '\n>')
        if classChoice in list_role[6:8]:
            print(f'{line}')
            print('Warrior Stats:'
                  '\nStrength +3'
                  '\nDefence +3')
            print(f'{line}')
            input('\nType any key to continue... >')
            print(f'\n{line}')
            print('Mage Stats:'
                  '\nIntelligence +3'
                  '\nMagic +3')
            print(f'{line}')
            input('\nType any key to continue... >')
            print(f'\n{line}')
            print('Archer Stats:'
                  '\nIntelligence +3'
                  '\nDexterity +3')
            print(f'{line}\n')

    return chooseClass(character, classChoice)


def chooseClass(character, choice):
    if choice in list_role[0:2]:
        character.classe = 'Warrior'
        character.strength += 3
        character.defence += 3

    elif choice in list_role[2:4]:
        character.classe = 'Mage'
        character.intelligence += 3
        character.magic += 3

    elif choice in list_role[4:6]:
        character.classe = 'Archer'
        character.intelligence += 3
        character.dexterity += 3


def game_start():
    character = Character.race_start()
    classDefinition(character)
    return character


# Criar habilidade de mago que cure ele
# Criar habilidade de guerreiro que aumente a defesa dele

