import random
from .magic import Spell
import pprint

class Person(object):
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def is_alive(self):
        return self.hp > 0

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + self.name)
        print("Choose an action")
        for item in self.actions:
            print(str(i), item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for item in self.magic:
            print(i, item.name, "(cost:", str(item.cost) + ")", "(dmg:", str(item.dmg) + ")")
            i += 1
        print("0 back to actions")

    def choose_item(self):
        i = 1
        print("Items")
        for item in self.items:
            print(i, item["item"].name, ":", item["item"].description, "x" + str(item["quantity"]))
            i += 1
        print("0 back to actions")

    def choose_target(self, enemies):
        i = 1
        print("Target")
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(str(i), enemy.name)
                i += 1
        choice = int(input("Choose Target: ")) - 1
        return choice

    def get_stats(self):
        print(self.name," " + str(self.hp) + "/" + str(self.maxhp), "   ", str(self.mp) + "/" + str(self.maxmp))

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        if self.mp < spell.cost:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
