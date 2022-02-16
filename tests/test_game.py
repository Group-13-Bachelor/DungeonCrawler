import pytest
import unittest
import random
from game.avatar import Avatar, Inventory
from game.item import Item
from game.dungeon import Dungeon, init_layout


class TestGame(unittest.TestCase):
    """Test class for game package"""

    @pytest.fixture
    def my_avatar():
        item = Item(1, 2, 3, 4)
        inventory = Inventory([item, item])
        return Avatar("Test", 10, 11, 12, 13, inventory)

    # avatar.move("North")
    # avatar.run()
    # @pytest.fixture
    # def my_enemy():
    #     return Enemy("Test", 10, 11, 12, 13)

    # def test_fight(my_avatar, my_enemy):
    #     health = my_enemy.health
    #     my_avatar.fight(my_enemy)
    #     assert my_enemy.health < health

    def test_generate_dungeon(self):
        """Generates a random dungeon 100 times with new seed, size and nr rooms each time"""
        dungeon = Dungeon()
        dungeon.use_seed = False    # Generate a new dungeon each time with the same object
        for _ in range(0, 1000):
            dungeon._width = random.randint(12, 36)
            dungeon._height = random.randint(12, 36)
            dungeon.layout = init_layout(dungeon._height, dungeon._width)
            dungeon.nr_rooms = random.randint(12, 16)
            dungeon.create_dungeon()


if __name__ == '__main__':
    unittest.main()     # This allows for infile testing with pytest
