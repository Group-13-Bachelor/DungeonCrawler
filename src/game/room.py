from pytest import Item
from game.entity import Entity
from game.avatar import Avatar


class Room:
    entities = list()
    item: Item

    def __init__(self, item: Item = None):
        self.item = item

    def add_entity(self, entity: Entity):
        self.entities.append(entity)

    def remove_entity(self, entity: Entity):
        self.entities.pop(entity)

    def take_item(self, avatar: Avatar):
        avatar.inventory.add_item(self.item)

    def __str__(self):
        return 'Room'


if __name__ == "__main__":
    item = Item("Item", )
    room = Room()
