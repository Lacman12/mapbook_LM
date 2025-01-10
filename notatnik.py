from tkinter.font import names


users: list = [
    {'name': 'Dominik', 'posts': 1, 'city': 'Poznań'},
    {'name': 'Julia', 'posts': 1, 'city': 'Zamość'},
    {'name': 'Patryk', 'posts': 11, 'city': 'Łódź'},
    {'name': 'Patrycja', 'posts': 11, 'city': 'Zielona_Góra'},
]
class User:
    def __init__(self, imie,nazwisko,posts,lokalizacja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.posts = posts
        self.lokalizacja = lokalizacja


user_Marek=User('Marek','a','3','a')

print(user_Marek.imie)
print(user_Marek.nazwisko)
print(user_Marek.posts)
print(user_Marek.lokalizacja)

