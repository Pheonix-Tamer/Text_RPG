import random


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.adjacent = {"north": None, "south": None, "east": None, "west": None}

    # def __repr__(self):
    #     return f"Room: {self.name}, {self.description}"


class ItemRoom(Room):
    def __init__(self, name, description, items=None):
        super().__init__(name, description)
        self.items = [] if items is None else items

    def add_item(self, x):
        self.items.append(x)

    def remove_item(self, x):
        self.items.remove(x)


class TrapRoom(Room):
    def __init__(
        self, name, description, damage_range: tuple[int, int], destination=None
    ):
        super().__init__(name, description)
        self.damage_range = damage_range
        self.destination = destination

    def calc_dmg(self) -> int:
        return random.randint(*self.damage_range)


class CombatRoom(Room):
    def __init__(self, name, description, monster_type, monster_damage):
        super().__init__(name, description)
        self.monster_type = monster_type
        self.monster_damage = monster_damage


class BossRoom(CombatRoom):
    def __init__(self, name, description, boss_name, boss_hp, boss_damage):
        super().__init__(name, description, "Boss", boss_damage)
        self.boss_name = boss_name
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage


# Rooms in dungeon
entrance = Room("Entrance", "A cave opening")
goblin_quarters = CombatRoom(
    "Goblin Quarters",
    "A room full of foul bedding for the goblins to sleep",
    "goblin",
    5,
)
corridor_1 = Room("Corridor", "An unassuming corridor with no distinguishing features")
fake_chests = TrapRoom("Fake Chests", "A room filled with chests.", (1, 4), entrance)
guard_room = CombatRoom(
    "Guard Room",
    "A small room with guard stations on both sides ready to pounce on intruders",
    "goblin",
    5,
)
lonely_goblin = ItemRoom(
    "Lonely Goblin",
    "A single sad looking goblin sits in the middle of the room playing with a dagger",
    ["dagger"],
)
treasure = ItemRoom(
    "Treasure",
    "A room with many stolen items from nearby towns",
    ["health potion", "chestplate", "helmet"],
)
corridor_2 = Room("Corridor", "An unassuming corridor with no distinguishing features")
spike_pit = TrapRoom(
    "Spike Pit", "A room with a poorly hidden pitfall blocking the way", (2, 8)
)
boss_room = BossRoom(
    "Boss Room", "The room where the leader of the goblins sleeps", "Gobo", 15, (2, 10)
)

# Setting directions
entrance.adjacent["north"] = corridor_1
entrance.adjacent["east"] = guard_room
entrance.adjacent["west"] = goblin_quarters

goblin_quarters.adjacent["east"] = entrance

corridor_1.adjacent["south"] = entrance
corridor_1.adjacent["east"] = fake_chests

fake_chests.adjacent["west"] = corridor_1

guard_room.adjacent["west"] = entrance
guard_room.adjacent["east"] = lonely_goblin

lonely_goblin.adjacent["west"] = guard_room
lonely_goblin.adjacent["north"] = corridor_2
lonely_goblin.adjacent["south"] = treasure

treasure.adjacent["north"] = lonely_goblin

corridor_2.adjacent["south"] = lonely_goblin
corridor_2.adjacent["east"] = spike_pit

spike_pit.adjacent["west"] = corridor_2
spike_pit.adjacent["south"] = boss_room

boss_room.adjacent["north"] = spike_pit
