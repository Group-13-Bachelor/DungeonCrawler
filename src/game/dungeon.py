from __future__ import annotations
from logging import log
from typing import List
import random

from game.room import Room
from game.entity import Entity


def static_dungeon():
    '''Returns static dungeon that is always the same'''
    return [
        [None,  Room(0, 1), Room(0, 2), None,       None,       None],
        [None,  Room(1, 1), Room(1, 2), None,       None,       None],
        [None,  None,       Room(2, 2), Room(2, 3), Room(2, 4), None],
        [None,  None,       None,       None,       Room(3, 4), Room(3, 5)],
        [None,  None,       None,       Room(4, 3),  Room(3, 4), None],
        [None,  None,       None,       Room(5, 3), None,       None]
        ]


def static_room_list(layout):
    rooms = []
    for row in layout:
        for room in row:
            if room is not None:
                rooms.append(room)
    return rooms


class Dungeon:
    _seed: int = 87264239876487236  # Default seed
    layout = [[]]
    rooms = []
    _width = 6
    _height = 6
    nr_rooms = 12*12
    use_seed: bool = True

    def __init__(self):
        self._seed = generate_seed()
        self.layout = init_layout(self._width, self._height)

    def create_dungeon(self):
        """Creates a dungeon based on settings"""
        if self.use_seed:
            random.seed(self._seed)
        height = random.randint(int(self._height/2) - 3, int(self._height/2) + 3)    # Start somewhere in the middle
        width = random.randint(int(self._width/2) - 3, int(self._width/2) + 3)
        self.create_room(height, width)

    def check_boundaries(self, _height, _width) -> bool:
        if (_height < self._height and _height > 0
                and _width < self._width and _width > 0):
            return True
        else:
            return False

    # BUG: infinite loop sometimes
    def create_room(self, height, width, nr_rooms=0, debug=True):
        """Simple recursion generating a room next to previos in random direction"""
        if not debug:
            rooms: List[Room] = []

            while nr_rooms < self.nr_rooms:
                direction = random.randint(0, 3)    # Choose direction

                _height, _width = get_direction(height, width, direction)
                if self.check_boundaries(_height, _width):
                    if self.layout[_height][_width] is None:
                        height = _height
                        width = _width
                        room = Room(height, width)
                        self.layout[height][width] = room
                        self.rooms.append(room)
                        rooms.append(self.layout[height][width])
                        nr_rooms = nr_rooms + 1
                    elif(rooms):
                        room: Room = rooms.pop()
                        height = room.x_pos
                        width = room.y_pos
                    else:
                        log(0, "Dungeon generation exit", rooms, height, width)
                        return
        else:
            self.layout = static_dungeon()
            self.rooms = static_room_list(self.layout)

    def get_entity_pos(self, entity):
        '''Returns position of given entity'''
        room = self.get_entity_room(entity)
        return room.x_pos, room.y_pos

    def get_entity_room(self, entity):
        '''Returns room of given entity'''
        for room in self.rooms:
            if room:
                for e in room.entities:
                    if entity == e:
                        return room
        print("Entity not found")

    def spawn_entity(self, entity):
        '''Adds entity to a random room'''
        i = random.randint(0, len(self.rooms) - 1)
        self.rooms[i].add_entity(entity)

    def add_entity(self, entity, xPos, yPos):
        self.layout[xPos][yPos].add_entity(entity)

    def remove_entity(self, entity):
        room = self.get_entity_room(entity)
        room.remove_entity(entity)

    def move_entity(self, entity, direction):
        xPos, yPos = self.get_entity_pos(entity)
        new_xPos, new_yPos = get_direction(xPos, yPos, direction)
        if self.layout[new_xPos][new_yPos] is not None:
            self.remove_entity(entity)
            self.add_entity(entity, new_xPos, new_yPos)

    def print_layout(self):
        print('\n'.join(['|'.join(['%s' % i for i in row]) for row in self.layout]))


def get_direction(height, width, direction):
    '''Returns grid position based on given x,y pos and direction'''
    switcher = {
        0: (height - 1, width),
        1: (height, width - 1),
        2: (height + 1, width),
        3: (height, width + 1)
    }
    return switcher.get(direction)


def generate_seed() -> int:
    seed = ''
    for _ in range(0, 16):
        seed += str(random.randint(0, 9))
    return int(seed)


def init_layout(height, width):
    """Creates a double list of given height and width"""
    return [[None for _ in range(width)] for _ in range(height)]


if __name__ == "__main__":
    dungeon = Dungeon()
    dungeon.create_dungeon()
    # dungeon.print_layout()
    entity = Entity("Test", 10, 11, 12, 13)
    entity2 = Entity("Test2", 20, 21, 22, 23)
    dungeon.spawn_entity(entity)
    dungeon.spawn_entity(entity2)
    print(dungeon.get_entity_pos(entity))
    print(dungeon.get_entity_room(entity))
    dungeon.print_layout()
    dungeon.move_entity(entity, 0)
    # print(dungeon.get_entity_pos(entity))
    # print(dungeon.get_entity_room(entity))
    dungeon.print_layout()
