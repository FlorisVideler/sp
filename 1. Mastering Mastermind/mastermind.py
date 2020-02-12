import random

colors = [
    {
        "Kleur": "Groen",
        "Afkorting": "G"
    },
    {
        "Kleur": "Rood",
        "Afkorting": "R"
    },
    {
        "Kleur": "Blauw",
        "Afkorting": "B"
    },
    {
        "Kleur": "Oranje",
        "Afkorting": "O"
    },
    {
        "Kleur": "Wit",
        "Afkorting": "W"
    },
    {
        "Kleur": "Paars",
        "Afkorting": "P"
    }
]

code_global = []


def menu():
    print("Welkom to mastermind!")
    gives_feedback = "n"
    while True:
        who_is_playing = input("Raadt de speler? (y/n) ")
        if who_is_playing.lower() == "y":
            break
        elif who_is_playing.lower() == "n":
            while True:
                gives_feedback = input("Geeft de pc feedback? (y/n) ")
                if gives_feedback.lower() == "y" or gives_feedback.lower() == "n":
                    break
            break
    return who_is_playing, gives_feedback


def pc_game():
    return


def player_game():
    # Set code
    code = random.sample(colors, k=4)
    set_code(code)
    print(code)


def set_code(code):
    code_global.clear()
    for i in code:
        code_global.append(i["Afkorting"])
    print(code_global)



def game():
    settings = menu()
    if settings[0] == "y":
        player_game()


game()
