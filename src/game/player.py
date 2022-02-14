from game.avatar import Avatar


class Player:
    name: str = "Player"
    avatar: Avatar

    def __init__(self, name: str, avatar: Avatar) -> None:
        self.name = name
        self.avatar = avatar
