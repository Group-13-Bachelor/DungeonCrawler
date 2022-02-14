class Item:
    def __init__(self, name: str, health: int, attack: int, defence: int, luck: int) -> None:
        self.name: str = name
        self.health: int = health
        self.attack: int = attack
        self.defence: int = defence
        self.luck: int = luck
