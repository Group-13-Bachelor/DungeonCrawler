from __future__ import annotations  # Pospone type evaluation, defualt behavior in 3.10import random
import random

from game.room import Room

# from game.room import Room


class Dungeon:
    _seed: int = 87264239876487236
    layout = [[]]
    _width = 12
    _height = 12
    nr_rooms = 6

    def __init__(self):
        self._seed = generate_seed()
        self.layout = [[None for _ in range(self._width)] for _ in range(self._height)]

    def create_dungeon(self):
        random.seed(self._seed)
        x = random.randint(self._height/2 - 3, self._height/2 + 3)    # Start somewhere in the middle
        y = random.randint(self._width/2 - 3, self._width/2 + 3)
        self.create_room(x, y)
        for _ in range(0, self.nr_rooms):
            x = random.randint(0, self._height - 1)    # Start somewhere in the middle
            y = random.randint(self._height, self._height - 1)
            self.create_room(x, y)

    def create_room(self, x, y):
        self.layout[x][y] = Room()

    def print_layout(self):
        print('\n'.join([''.join(['%s' % i for i in row]) for row in self.layout]))


def generate_seed() -> int:
    seed = ''
    for _ in range(0, 16):
        seed += str(random.randint(0, 9))
    return int(seed)


if __name__ == "__main__":
    dungeon = Dungeon()
    dungeon.create_dungeon()
    dungeon.print_layout()
