class Avatar:
    attack: int = 0
    health: int = 0
    defence: int = 0
    luck: int = 0

    def __init__(self, attack: int, health: int, defence: int, luck: int) -> None:
        self.attack: int = attack
        self.health: int = health
        self.defence: int = defence
        self.luck: int = luck

    def move(direction):
        pass

    def fight(target: Enemy):
        pass

    def run():
        pass

    def equip_item(item: Item):
        pass

    def dequip_item(item: Item):
        pass


if __name__ == "__main__":
    pass
