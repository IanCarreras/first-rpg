from classes.game import Person
import random
from classes.magic import Spell
from classes.inventory import Item
import classes.magic as magic

def play():

    potion = Item("Potion", "potion", "Heals 50 HP", 50)
    hipotion = Item("Hi-potion", "potion", "Heals 100 HP", 100)
    superpotion = Item("Super-potion", "potion", "Heals 500 HP", 500)
    elixir = Item("Elixir", "elixir", "Fully restores HP and MP of one party member", 99999)
    megaelixir = Item("Mega-elixir", "elixir", "Fully restores HP and MP of party", 99999)

    grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

    player_magic = [magic.Fire(), magic.Thunder(), magic.Meteor(), magic.Cura()]
    player_items = [{"item": potion, "quantity": 10},
                    {"item": superpotion, "quantity": 3},
                    {"item": grenade, "quantity": 2}]

    player = Person(460, 65, 60, 34, player_magic, player_items)
    enemy = Person(1200, 65, 45, 25, [], [])

    running = True

    print("=============================")
    print("You have encountered an enemy")
    while running:
        print("=============================")
        player.choose_action()
        choice = input()
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked the enemy for", dmg, "dmg")
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
                print("Player casts", spell.name, "and heals for", str(magic_dmg), "HP")
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print("Player casts", spell.name, "and deals", str(magic_dmg), "dmg")
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
                print("Player uses", item.name, "heals for", item.prop, "HP")
            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print("Player uses", item.name, " and fully restores HP and MP")
            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print("Player uses", item.name, "and deals", item.prop, "dmg")



        enemy_choice = 1

        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacked you and dealt", enemy_dmg, "dmg")

        print("------------")
        print("Enemy HP:", str(enemy.get_hp()))
        print("Player1 HP:", str(player.get_hp()))
        print("Player1 MP:", str(player.get_mp()))

        if enemy.is_alive() == False:
            print("Victory! You have defeated the enemy!")
            running = False

        if player.is_alive() == False:
            print("You have been defeated!")
            running = False

play()
