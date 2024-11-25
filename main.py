users: list = [
    {'name': 'Michał', 'posts': 1, 'city': 'Warszawa'},
    {'name': 'Dominik', 'posts': 3, 'city': 'Poznań'},
    {'name': 'Szymon z wąsem', 'posts': 5, 'city': 'Toruń'},
    {'name': 'Szymon', 'posts': 7, 'city': 'łódź'},
    {'name': 'Patryk', 'posts': 9, 'city': 'Kielce'},

]  # typizacja zmiennych bedzie przechowywac liste
#TODO please update user list

print(f'Witaj {users[0]['name']}!!')
for user in users[1:]:#wybiera wszystkich oprócz 0, ważny : po numerze
   print(f'twój znajomy {user['name']},z miasta {user['city']} opublikował {user['posts']} postów')# f oznacza format - zastepuje to co jest w nawasie zmienną
# for idx, _ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
