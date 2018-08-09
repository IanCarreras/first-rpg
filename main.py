from classes.characters import Person
import random
from classes.magic import Spell
from classes.items import Item
import classes.magic as Magic
import classes.items as Items


def play():

    player_magic = [Magic.Fire(), Magic.Thunder(), Magic.Meteor(), Magic.Cura()]
    player_items = [{"item": Items.Potion(), "quantity": 10},
                    {"item": Items.SuperPotion(), "quantity": 3},
                    {"item": Items.Grenade(), "quantity": 2}]

    player1 = Person("Runner    ", 460, 65, 60, 34, player_magic, player_items)
    player2 = Person("Witness   ", 460, 65, 60, 34, player_magic, player_items)
    player3 = Person("Novelist  ", 460, 65, 60, 34, player_magic, player_items)
    player4 = Person("Zealot    ", 460, 65, 60, 34, player_magic, player_items)
    enemy1 = Person("Baba-Yaga  ", 1400, 65, 45, 25, [Magic.Fire()], [])
    enemy2 = Person("Eld Fen    ", 1600, 65, 45, 25, [Magic.Meteor()], [])
    enemy3 = Person("Parzival   ", 1200, 65, 45, 25, [Magic.Thunder()], [])

    players = [player1, player2, player3, player4]
    enemies = [enemy1, enemy2, enemy3]
    enemy = random.randrange(0, 3)

    running = True

    print("================================")
    print("You have encountered " + enemies[enemy].name)
    print("================================")


    while running:
        print("\n")
        print("                    HP       MP")
        for enemy in enemies:
            enemy.get_stats()
        print("\n")
        print("                 HP       MP")
        for player in players:
            player.get_stats()

        print("\n")
        for player in players:
            player.choose_action()
            choice = input()
            index = int(choice) - 1

            if index == 0:
                dmg = player.generate_damage()
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)
                print("======================================")
                print("The " + player.name.strip() + " attacked " + enemies[enemy].name.strip() + " for", dmg, "dmg")

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name, " has been defeated")
                    del enemies[enemy]
            elif index == 1:
                player.choose_magic()
                magic_choice = int(input("Choose magic: ")) - 1

                if magic_choice == -1:
                    continue

                magic_dmg = player.magic[magic_choice].generate_damage()
                spell = player.magic[magic_choice]
                current_mp = player.get_mp()

                if spell.cost > current_mp:
                    print("Not enough MP")
                    continue

                player.reduce_mp(spell.cost)

                if spell.type == "white":
                    player.heal(magic_dmg)
                    print("======================================")
                    print(player.name.strip() + " casts", spell.name, "and heals for", str(magic_dmg), "HP")
                elif spell.type == "black":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(magic_dmg)
                    print("======================================")
                    print(player.name.strip() + " casts", spell.name, "and deals", str(magic_dmg), "dmg to ", enemies[enemy].name)
                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name, " has been defeated")
                        del enemies[enemy]

            elif index == 2:
                player.choose_item()
                item_choice = int(input("Choose item: ")) - 1

                if item_choice == -1:
                    continue

                item = player.items[item_choice]["item"]

                if player.items[item_choice]["quantity"] == 0:
                    print("None left")
                    continue

                player.items[item_choice]["quantity"] -= 1

                if item.type == "potion":
                    player.heal(item.prop)
                    print("======================================")
                    print(player.name.strip() + " uses", item.name, "heals for", item.prop, "HP")
                elif item.type == "elixir":

                    if item.name == "Mega-elixir":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                    print("======================================")
                    print(player.name.strip() + " uses", item.name, " and fully restores HP and MP")
                elif item.type == "attack":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(item.prop)
                    print("======================================")
                    print(player.name.strip() + " uses", item.name, "and deals", item.prop, "dmg to ", enemies[enemy].name)

                    if enemies[enemy].get_hp() == 0:
                        print(enemies[enemy].name, " has been defeated")
                        del enemies[enemy]

        defeated_enemies = 0
        defeated_players = 0

        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeated_enemies += 1

        for player in players:
            if player.get_hp() == 0:
                defeated_players += 1

        if defeated_players == 2:
            print("======================================")
            print("Victory! You have defeated the enemy!")
            print("======================================")
            running = False

        if defeated_players == 2:
            print("======================================")
            print("You have been defeated!")
            print("======================================")
            running = False

        for enemy in enemies:
            enemy_choice = random.randrange(0, 2)

            if enemy_choice == 0:
                target = random.randrange(0, 3)
                enemy_dmg = enemies[0].generate_damage()
                players[target].take_damage(enemy_dmg)
                print("======================================")
                print(enemy.name.strip() + " attacked the " + players[target].name.strip() + " and dealt", enemy_dmg, "dmg")

            elif enemy_choice == 1:
                spell, magic_dmg = enemy.choose_enemy_spell()
                enemy.reduce_mp(spell.cost)

                elif spell.type == "black":
                    target = random.randrange(0, 3)
                    players[target].take_damage(magic_dmg)
                    print("======================================")
                    print(enemy.name.strip() + " casts", spell.name, "and deals", str(magic_dmg), "dmg to the", players[target].name)
                    if players[target].get_hp() == 0:
                        print(players[taget].name, " has been defeated")
                        del players[player]


play()
