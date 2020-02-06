import random


def play_game():
    guess = random.randint(1, 9)
    # If you want 2 cheat
    # print(guess)
    while True:
        inp = int(input("Getal tussen 0 en 10: "))
        if inp == guess:
            return "Winner"


print(play_game())
