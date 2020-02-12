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
    board = ""
    steps = 0
    # Set code
    code = random.sample(colors, k=4)
    set_code(code)
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n=========================================================")
        print(board)
        guess_input = input("Do een gok: ")
        try:
            guess_list = guess_input.upper().replace(" ", "").split(",")
            #print(guess_list)
            guess_response = auto_feedback(guess_list)
            steps += 1
            right_color_str = ""
            if guess_response[0] > 0:
                right_color_str = "?" * guess_response[0]
            right_place_str = ""
            if guess_response[1] > 0:
                right_place_str = "!" * guess_response[1]
            board += "{:^10} {:^10} {:^10} {:^10} || {:^10} {:^10}\n".format(guess_list[0], guess_list[1], guess_list[2], guess_list[3], right_color_str, right_place_str)
            if guess_response[1] == 4:
                print(f"WINNER WINNER CHICKEN DINNER.\nJE HEBT DE CODE GERADEN IN {steps} STAPPEN!")
                break
            #print(guess_response)
        except:
            print("GEEN GELDIGE INPUT!")


def auto_feedback(guesslst):
    #Check if color is in code
    right_color = 0
    right_place = 0
    for g, color in enumerate(guesslst):
        if color in code_global:
            if code_global[g] == guesslst[g]:
                right_place += 1
            else:
                right_color += 1
    return right_color, right_place


def set_code(code):
    code_global.clear()
    for i in code:
        code_global.append(i["Afkorting"])
    print("Code is set!")
    print(code_global)



def game():
    settings = menu()
    if settings[0] == "y":
        player_game()


game()
