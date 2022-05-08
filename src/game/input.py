from game import avatar

def read():
    return input("Input:\t").lower()


def main_menu(i: str):
    if i == '1':
        scan()
    elif i == '2':
        display_avatar()
    elif i == '3':
        display_players()
    elif i == '4':
        join_dungeon()

    return (
        "1. Scan Network" + '\n'
        "2. Display Avatar" + '\n'
        "3. Display Players" + '\n'
        "4. Join Dungeon" '\n'
    )


def game_menu():
    return (
        "1. Fight" + '\n'
        "2. Run" + '\n'
        "3. Move + direction(up, down, left, right)" + '\n'
        "4. Leave Dungeon" '\n'
    )


def main():
    ext = "9. Exit \n"
    state = "Menu"
    i = ''
    while i != '9' and i != 'Exit'.lower():
        if state == "Menu":
            print(main_menu(i) + ext)
        if state == "Game":
            print(game_menu(i) + ext)
        i = read()


def scan():
    pass


def display_avatar():
    print(avatar.Avatar("Jordan", 100, 10, 10, 3, []))


def display_players():
    pass


def join_dungeon():
    pass


def fight():
    print("Fight!\n")


def run():
    pass


def move():
    pass


def leave_dungeon():
    pass

if __name__ == "__main__":
    main()
