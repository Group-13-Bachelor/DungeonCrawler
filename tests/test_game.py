import pytest
from game.avatar import Avatar, Inventory
from game.enemy import Enemy
from game.item import Item
import unittest


class TestGame(unittest.TestCase):
    """Test class for game package"""

    @pytest.fixture
    def my_avatar():
        item = Item(1, 2, 3, 4)
        inventory = Inventory([item, item])
        return Avatar("Test", 10, 11, 12, 13, inventory)

    # avatar.move("North")
    # avatar.run()
    @pytest.fixture
    def my_enemy():
        return Enemy("Test", 10, 11, 12, 13)

    def test_fight(my_avatar, my_enemy):
        health = my_enemy.health
        my_avatar.fight(my_enemy)
        assert my_enemy.health < health


if __name__ == '__main__':
    unittest.main()     # This allows for infile testing with pytest
