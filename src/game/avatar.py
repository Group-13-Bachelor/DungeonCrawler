from __future__ import annotations  # Pospone type evaluation, defualt behavior in 3.10
from typing import List

from game.entity import Entity
from game.item import Item


class Avatar(Entity):
    inventory: Inventory
    _previous_direction = ''    # direction player came from

    def __init__(self, name: str, health: int, attack: int, defence: int, luck: int, inventory: List[Item]):
        super().__init__(name, health, attack, defence, luck)
        self.inventory = Inventory(inventory)

    def move(self, direction):
        self._previous_direction = direction
        super().move(direction)

    def run(self):
        switcher = {
            "North": "South",
            "South": "North",
            "East": "West",
            "West": "East"
        }
        super().move(switcher.get(self._previous_direction))

    def equip_item(self, item: Item):
        self.health = self.health + item.health
        self.attack = self.attack + item.attack
        self.defence = self.defence + item.defence
        self.luck = self.luck + item.luck

    def dequip_item(self, item: Item):
        self.health = self.health - item.health
        self.attack = self.attack - item.attack
        self.defence = self.defence - item.defence
        self.luck = self.luck - item.luck

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self):
        return super().__str__() + f"{self.inventory.inventory}"


class Inventory:
    inventory: List[Item] = list()

    def add_item(self, item: Item):
        self.inventory.append(item)

    def remove_item(self, item: Item):
        self.inventory.pop(item)

    def __init__(self, inventory: List[Item]):
        self.inventory = inventory

    def __str__(self) -> str:
        return f"Inventory{self.inventory}"


if __name__ == "__main__":
    pass
