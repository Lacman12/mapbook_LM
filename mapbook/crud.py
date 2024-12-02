


def hello(user:str)->None:
    print(f'Witaj {user}!!')

def read_users(users:list)->None:
    for user in users[1:]:  # wybiera wszystkich oprócz 0, ważny : po numerze
        print(f'twój znajomy {user['name']},z miasta {user['city']} opublikował {user['posts']} postów')  # f oznacza format - zastepuje to co jest w nawasie zmienną


def add_user(userlist:list)->None:
    new_name:str=input('Proszę podać imię nowego znajomego ')
    new_posts:int=int(input('podaj liczbę postów nowego znajomego '))
    new_city:str=input('Podaj miasto ')
    new_user: dict = {'name': new_name, 'posts':new_posts, 'city': new_city}
    userlist.append(new_user)


def remove_user(userlist:list)->None:
    user_to_find:str=input('podaj imię osoby do usunięcia: ')
    for user in userlist:
        if user['name'] == user_to_find:
            print(f'usuwam: {user}')
            userlist.remove(user)

def update_user(userlist:list)->None:
    user_to_find:str=input('podaj imię użytkownika do aktualizacji: ')
    for user in userlist:
            if user['name'] == user_to_find:
                new_name:str=input('Proszę podać nowe imię  znajomego ')
                new_posts:int=int(input('podaj nową liczbę postów znajomego '))
                new_city:str=input('Podaj nowe miasto ')
                user['name']=new_name
                user['posts']=new_posts
                user['city']=new_city