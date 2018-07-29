from classes.game import Person
import random


magic = [{"name": "Fire", "cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 10, "dmg": 60},
    {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

is_alive = True
i = 0

while is_alive:
    print("===================")
    player.choose_magic()
    choice = input("Choose action: ")
    index = int(choice) - 1

    print("You chose: ", index)

    is_alive = False

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())

print(player.generate_spell_damage(random.randrange(0, len(magic))))
print(player.generate_spell_damage(random.randrange(0, len(magic))))
print(player.generate_spell_damage(random.randrange(0, len(magic))))
