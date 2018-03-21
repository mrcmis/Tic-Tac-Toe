from board import Board
from gameplay import Gameplay

#w 'konstruktorze' na ta chwile mozna sobie ustawiac wartosci pol i tam tez wyswietlam plansze
gameplay = Gameplay()

if gameplay.is_win():
    print("TAK")
else:
    print("NIE")

