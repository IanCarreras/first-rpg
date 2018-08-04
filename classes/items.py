class Item(object):
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop

class Potion(Item):
    def __init__(self):
        Item.__init__(
            self,
            name="Potion",
            type="potion",
            description="Heals 50 HP",
            prop=50,
        )

class HiPotion(Item):
    def __init__(self):
        Item.__init__(
            self,
            name="Hi-Potion",
            type="potion",
            description="Heals 100 HP",
            prop=100,
        )

class SuperPotion(Item):
    def __init__(self):
        Item.__init__(
            self,
            name="Super-Potion",
            type="potion",
            description="Heals 500 HP",
            prop=500,
        )

class Elixir(Item):
    def __init__(self):
        Item.__init__(
            self,
            name="Elixir",
            type="elixir",
            description="Fully restores HP and MP of one party member",
            prop=99999,
        )

class MegaElixir(Item):
    def __init__(self):
        Item.__init__(
            self,
            name="Mega-elixir",
            type="elixir",
            description="Fully restores HP and MP of entire party",
            prop=99999,
        )

class Grenade(Item):
    def __init__(self):
        Item.__init__(
            self,
            name="Grenade",
            type="attack",
            description="Deals 500 damage",
            prop=500,
        )
