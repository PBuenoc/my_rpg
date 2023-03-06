list_choices = ['s', 'S', 'f', 'F', 'a', 'A']
list_op = ['l', 'L', 'V', 'v', 'ms', 'MS', 'd', 'D']


def combat(character, monster):
    character_turn = True
    print('=========== O combate começou!! ===========')
    while character.life > 0 and monster.life > 0:
        if character_turn is True:
            print(f'Turno de {character.name}!')
            character_choice = input(f'{character.name}, o que irá fazer?'
                                     f'\nLutar: [l/L]'
                                     f'\nVer seus status: [v/V]'
                                     f'\nVer status do monstro: [ms/MS]'
                                     f'\nDesistir: [d/D]'
                                     f'\n>')
            while character_choice not in list_op:
                character_choice = input(f'Opição inválida! Escolha novamente:'
                                         f'\nLutar: [l/L]'
                                         f'\nVer seus status: [v/V]'
                                         f'\nVer status do monstro: [ms/MS]'
                                         f'\nDesistir: [d/D]'
                                         f'\n>')
            else:
                pass
            if character_choice in list_op[0:2]:
                print('\nVocê escolheu Lutar!!')
                attack_choice = input('Qual será seu ataque?'
                                      '\nSoco [s/S]'
                                      '\nFeitiço [f/F]'
                                      '\nAtirar flecha [a/A]'
                                      '\n> ')
                if monster.life <= 0:
                    print('Voçê venceu!!')
                    print(f'+{monster.xp}xp')
                    character.xp += monster.xp
                else:
                    if attack_choice in list_choices[0:2]:
                        attack = character.punch_attack()
                        if attack != 'Errou!':
                            character_damage = attack - monster.defence
                            monster.life -= character_damage
                            if monster.life <= 0:
                                print(f'Monster HP: 0/{monster.max_life}'
                                      f'\n{character.name} deu {character_damage} de dano!'
                                      f'\n==========================')
                                monster.life = 0
                            else:
                                print(f'Monster HP: {monster.life}/{monster.max_life}'
                                      f'\n{character.name} deu {character_damage} de dano!'
                                      f'\n==========================')
                            character_turn = False
                        else:
                            print(attack)
                            character_turn = False
                    elif attack_choice in list_choices[2:4]:
                        attack = character.spell_attack()
                        if attack != "Você não pode lançar o feitiço!":
                            character_damage = attack - monster.defence
                            monster.life -= character_damage
                            if monster.life <= 0:
                                print(f'Monster HP: 0/{monster.max_life}'
                                      f'\n{character.name} deu {character_damage} de dano!'
                                      f'\n==========================')
                                monster.life = 0
                            else:
                                print(f'Monster HP: {monster.life}/{monster.max_life}'
                                      f'\n{character.name} deu {character_damage} de dano!'
                                      f'\n==========================')
                            character_turn = False
                        else:
                            print(attack)
                            character_turn = False
                    elif attack_choice in list_choices[4:6]:
                        attack = character.arrow_attack()
                        if attack != "Errou! Você está sem sorte!" or "Errou!":
                            character_damage = attack - monster.defence
                            monster.life -= character_damage
                            if monster.life <= 0:
                                print(f'Monster HP: 0/{monster.max_life}'
                                      f'\n{character.name} deu {character_damage} de dano!'
                                      f'\n==========================')
                                monster.life = 0
                            else:
                                print(f'Monster HP: {monster.life}/{monster.max_life}'
                                      f'\n{character.name} deu {character_damage} de dano!'
                                      f'\n==========================')
                            character_turn = False
                        else:
                            print(attack)
                            character_turn = False
            elif character_choice in list_op[2:4]:
                print(f'{character.print_stats()}')
                continue
            elif character_choice in list_op[4:6]:
                print(f'{monster.print_monster_stats()}')
                continue
            elif character_choice in list_op[6:8]:
                print('Você desistiu de lutar e morreu!'
                      '\nFim da campanha')
                character.life = 0
                break
        elif character_turn is False:
            print('Turno do monstro!')
            monster_damage = monster.damage - character.defence
            character.life -= monster_damage
            print(f'{character.name}'
                  f'\nHP: {character.life}/{character.max_life}'
                  f'\nO monstro deu {monster_damage} de dano!'
                  f'\n==========================')
            if character.life > 0:
                print(f'Turno de {character.name}!')
                character_choice = input(f'{character.name}, o que irá fazer?'
                                         f'\nLutar: [l/L]'
                                         f'\nVer seus status: [v/V]'
                                         f'\nVer status do monstro: [ms/MS]'
                                         f'\nDesistir: [d/D]'
                                         f'\n>')
                while character_choice not in list_op:
                    character_choice = input(f'Opição inválida! Escolha novamente:'
                                             f'\nLutar: [l/L]'
                                             f'\nVer seus status: [v/V]'
                                             f'\nVer status do monstro: [ms/MS]'
                                             f'\nDesistir: [d/D]'
                                             f'\n>')
                else:
                    pass
                if character_choice in list_op[0:2]:
                    print('\nVocê escolheu Lutar!!')
                    attack_choice = input('Qual será seu ataque?'
                                          '\nSoco [s/S]'
                                          '\nFeitiço [f/F]'
                                          '\nAtirar flecha [a/A]'
                                          '\n> ')
                    if monster.life <= 0:
                        print('Voçê venceu!!')
                        print(f'+{monster.xp}xp')
                        character.xp += monster.xp
                    else:
                        if attack_choice in list_choices[0:2]:
                            attack = character.punch_attack()
                            if attack != 'Errou!':
                                character_damage = attack - monster.defence
                                monster.life -= character_damage
                                if monster.life <= 0:
                                    print(f'Monster HP: 0/{monster.max_life}'
                                          f'\n{character.name} deu {character_damage} de dano!'
                                          f'\n==========================')
                                    monster.life = 0
                                else:
                                    print(f'Monster HP: {monster.life}/{monster.max_life}'
                                          f'\n{character.name} deu {character_damage} de dano!'
                                          f'\n==========================')
                                character_turn = False
                            else:
                                print(attack)
                                character_turn = False
                        elif attack_choice in list_choices[2:4]:
                            attack = character.spell_attack()
                            if attack != "Você não pode lançar o feitiço!":
                                character_damage = attack - monster.defence
                                monster.life -= character_damage
                                if monster.life <= 0:
                                    print(f'Monster HP: 0/{monster.max_life}'
                                          f'\n{character.name} deu {character_damage} de dano!'
                                          f'\n==========================')
                                    monster.life = 0
                                else:
                                    print(f'Monster HP: {monster.life}/{monster.max_life}'
                                          f'\n{character.name} deu {character_damage} de dano!'
                                          f'\n==========================')
                                character_turn = False
                            else:
                                print(attack)
                                character_turn = False
                        elif attack_choice in list_choices[4:6]:
                            attack = character.arrow_attack()
                            if attack != "Errou! Você está sem sorte!" or "Errou!":
                                character_damage = attack - monster.defence
                                monster.life -= character_damage
                                if monster.life <= 0:
                                    print(f'Monster HP: 0/{monster.max_life}'
                                          f'\n{character.name} deu {character_damage} de dano!'
                                          f'\n==========================')
                                    monster.life = 0
                                else:
                                    print(f'Monster HP: {monster.life}/{monster.max_life}'
                                          f'\n{character.name} deu {character_damage} de dano!'
                                          f'\n==========================')
                                character_turn = False
                            else:
                                print(attack)
                                character_turn = False
                elif character_choice in list_op[2:4]:
                    print(f'{character.print_stats()}')
                    continue
                elif character_choice in list_op[4:6]:
                    print(f'{monster.print_monster_stats()}')
                    continue
                elif character_choice in list_op[6:8]:
                    print('Você desistiu de lutar e morreu!'
                          '\nFim da campanha')
                    character.life = 0
                    break
