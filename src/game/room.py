from pytest import Item
from game.entity import Entity
from game.avatar import Avatar


class Room:
    entities = []
    item: Item
    x_pos: int
    y_pos: int

    def __init__(self, x_pos, y_pos, item: Item = None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.item = item
        self.entities = []

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def remove_entity(self, entity: Entity):
        self.entities.remove(entity)

    def take_item(self, avatar: Avatar):
        avatar.inventory.add_item(self.item)

    def __str__(self):
        if len(self.entities) == 0:
            return '[--]'
        else:
            return f'{self.entities}'


if __name__ == "__main__":
    item = Item("Item", )
    room = Room()
