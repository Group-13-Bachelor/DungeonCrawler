from __future__ import annotations  # Pospone type evaluation, defualt behavior in 3.10
import random


class Entity:
    name: str = "Entity"    # Entity default name
    attack: int = 0
    health: int = 0
    defence: int = 0
    luck: int = 0

    def __init__(self, name: str, health: int, attack: int, defence: int, luck: int) -> None:
        self.name = name
        self.health: int = health
        self.attack: int = attack
        self.defence: int = defence
        self.luck: int = luck

    def move(self, direction):
        print(direction)

    def fight(self, target: Entity):
        self_roll = self.roll
        target_roll = target.roll
        if self_roll < target_roll:
            damage = (self.attack / (target_roll * 0.1) - target.defence)
        else:
            damage = (self.attack * (self_roll * 0.1) - target.defence)
        target.health - damage

    def roll(self) -> float:
        return random.randint(10, 10, + self.luck)

    def __str__(self) -> str:
        return f"""
        Health: {self.health}, \n
        Attack: {self.attack}, \n
        Defence: {self.defence}, \n
        Luck: {self.luck}, \n
        """

    def __repr__(self) -> str:
        return f'{self.name}'


if __name__ == "__main__":
    entity = Entity("Test", 10, 11, 12, 13)
    pass
