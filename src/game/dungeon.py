from __future__ import annotations
from logging import log  # Pospone type evaluation, defualt behavior in 3.10import random
from typing import List
import random

from game.room import Room


class Dungeon:
    _seed: int = 87264239876487236  # Default seed
    layout = [[]]
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

# BUG: infinite loop sometimes
    def create_room(self, height, width, nr_rooms=0):
        """Simple recursion generating a room next to previos in random direction"""
        def check_boundaries(_height, _width) -> bool:
            if (_height < self._height and _height > 0
                    and _width < self._width and _width > 0):
                return True
            else:
                return False

        rooms: List[Room] = []

        while nr_rooms < self.nr_rooms:
            switcher = {
                0: (height - 1, width),
                1: (height, width - 1),
                2: (height + 1, width),
                3: (height, width + 1)
            }
            direction = random.randint(0, 3)    # Choose direction
            # if direction == 0 and height > 0:
            #     self.create_room(height - 1, width, nr_rooms + 1)
            # elif direction == 1 and width > 0:
            #     self.create_room(height, width - 1, nr_rooms + 1)
            # elif direction == 2 and height + 1 < self._height:
            #     self.create_room(height + 1, width, nr_rooms + 1)
            # elif direction == 3 and width + 1 < self._width:
            #     self.create_room(height, width + 1, nr_rooms + 1)

            _height, _width = switcher.get(direction)
            if check_boundaries(_height, _width):
                if self.layout[_height][_width] is None:
                    height = _height
                    width = _width
                    self.layout[height][width] = Room(height, width)
                    rooms.append(self.layout[height][width])
                    nr_rooms = nr_rooms + 1
                elif(rooms):
                    room: Room = rooms.pop()
                    height = room.x_pos
                    width = room.y_pos
                else:
                    log(0, "Dungeon generation exit", rooms, height, width)
                    return

    def check_direction(self, height, width, direction) -> bool:
        switcher = {
            0: (height - 1, width),
            1: (height, width - 1),
            2: (height + 1, width),
            3: (height, width + 1)
        }
        _height, _width = switcher.get(direction)
        self.create_room(switcher.get(direction))
        print(_height, '\n', _width)

    def print_layout(self):
        print('\n'.join(['|'.join(['%s' % i for i in row]) for row in self.layout]))


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
    dungeon.print_layout()
    # dungeon.check_direction(10, 5, 3)
