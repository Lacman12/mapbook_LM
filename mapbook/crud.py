


def hello(user:str)->None:
    print(f'Witaj {user}!!')

def read_users(users:list)->None:
    for user in users[1:]:  # wybiera wszystkich oprócz 0, ważny : po numerze
        print(f'twój znajomy {user['name']},z miasta {user['city']} opublikował {user['posts']} postów')  # f oznacza format - zastepuje to co jest w nawasie zmienną
