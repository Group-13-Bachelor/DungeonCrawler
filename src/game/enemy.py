class Enemy:
    attack: int = 0
    health: int = 0
    defence: int = 0
    luck: int = 0

    def __init__(self, health: int, attack: int, defence: int, luck: int) -> None:
        super().__init__(health, attack, defence, luck)


if __name__ == "__main__":
    pass
