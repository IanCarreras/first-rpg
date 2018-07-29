import random

class Spell(object):
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

class Fire(Spell):
    def __init__(self):
        Spell.__init__(
            self,
            name="Fire",
            cost=10,
            dmg=100,
            type="black"
        )

class Thunder(Spell):
    def __init__(self):
        Spell.__init__(
            self,
            name="Thunder",
            cost=10,
            dmg=100,
            type="black"
        )

class Blizzard(Spell):
    def __init__(self):
        Spell.__init__(
            self,
            name="Blizzard",
            cost=10,
            dmg=100,
            type="black"
        )

class Quake(Spell):
    def __init__(self):
        Spell.__init__(
            self,
            name="Quake",
            cost=15,
            dmg=150,
            type="black"
        )

class Meteor(Spell):
    def __init__(self):
        Spell.__init__(
            self,
            name="Meteor",
            cost=20,
            dmg=200,
            type="black"
        )

class Cure(Spell):
    def __init__(self):
        Spell.__init__(
            self,
            name="Cure",
            cost=12,
            dmg=120,
            type="white"
        )

class Cura(Spell):
    def __init__(self):
        Spell.__init__(
            self,
            name="Cura",
            cost=18,
            dmg=200,
            type="white"
        )
