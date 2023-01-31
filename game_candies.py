max_total = 150
total = max_total
game = False
duel = []
current = 0


def pvp_add_player(text: int):
    global duel
    duel.append(text)
    return duel


def duel_player(num: int):
    global duel
    return duel[num]


def current_player(num: int):
    global current
    current = num
    return current


def enemy_id():
    global duel
    global current
    if current == duel[0]:
        return duel[1]
    else:
        return duel[0]


def switch_players():
    global duel
    global current
    if current == duel[0]:
        current = duel[1]
    else:
        current = duel[0]


def set_total(num: int):
    global max_total
    max_total = num


def get_total() -> int:
    global total
    return total


def take_candies(take: int):
    global total
    total -= take


def check_game():
    global game
    return game


def new_game():
    global game
    global total
    if game:
        game = False
    else:
        game = True
        total = max_total
