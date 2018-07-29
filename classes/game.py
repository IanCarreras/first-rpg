import random
from .magic import Spell
import pprint

class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
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
        print("Actions")
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
