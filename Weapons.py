# A file for the weapon class and distinct weapons
import random


class Weapon:
    status_damage_dict = {
        None: None,
        "fire": (1, 6),
        "lightning": (1, 4),
        "cold": (1, 6),
    }

    def __init__(
        self, name: str, damage_range: tuple[int, int], status_effect: str = None
    ) -> None:
        self.name = name
        self.damage_range = damage_range
        self.average_damage = self.calc_average_dmg()
        self.status_effect: str = status_effect
        self.status_damage = self.status_damage_dict.get(
            self.status_effect, self.status_damage_dict[None]
        )

    def calc_damage(self) -> int:
        return random.randint(*self.damage_range)

    def calc_average_dmg(self) -> float:
        low, high = self.damage_range
        total = 0
        for num in range(low, high + 1):
            total += num
        return total / high

    def set_status(self, s=None):
        self.status_effect = s
        self.status_damage = self.status_damage_dict.get(
            s, self.status_damage_dict[None]
        )

    def inflict_status(self, entity):
        if self.status_effect is not None:
            entity.status_effects.append(self.status_effect)

    def __repr__(self):
        if self.status_effect is None:
            return f"{self.name} with {self.damage_range}, {self.average_damage} dmg"
        else:
            return f"{self.name} of {self.status_effect} with {self.damage_range}, {self.average_damage} dmg + {self.status_damage}"


longsword = Weapon("Longsword", (1, 8))
dagger = Weapon("Dagger", (1, 4))
battleaxe = Weapon("Battle Axe", (1, 12))
great_sword = Weapon("Great Sword", (2, 12))
