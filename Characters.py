from Weapons import *


class Entity:
    def __init__(self, name, hp=0):
        self.name = name
        self.hp = hp
        self.status_effects = []

    def add_status_effect(self, x):
        self.status_effects.append(x)


class Monster(Entity):
    def __init__(self, name, hp, weapon: Weapon):
        super().__init__(name, hp)
        self.weapon = weapon


class Boss(Monster):
    def __init__(self, name, hp, weapon, boss_name):
        super().__init__(name, hp, weapon)
        self.boss_name = boss_name


class Player(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.mp = 0
        self.class_type = "fighter"
        self.curr_weapon = None
        self.inventory = []
