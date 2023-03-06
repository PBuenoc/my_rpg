from Version01 import Character, Combat
import Monster

character = Character.game_start()
monster = Monster.combat_difficult('Noob')
Combat.combat(character, monster)
