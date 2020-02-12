import random

colors = [
    {
        "Kleur": "Groen",
        #"Afkorting": "G"
        "Afkorting": "1"
    },
    {
        "Kleur": "Rood",
        #"Afkorting": "R"
        "Afkorting": "2"
    },
    {
        "Kleur": "Blauw",
        "Afkorting": "3"
        #"Afkorting": "B"
    },
    {
        "Kleur": "Oranje",
        #"Afkorting": "O"
        "Afkorting": "4"
    },
    {
        "Kleur": "Wit",
        #"Afkorting": "W"
        "Afkorting": "5"
    },
    {
        "Kleur": "Paars",
        "Afkorting": "1"
        #"Afkorting": "P"
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
                    if gives_feedback.lower() == "n":
                        gives_feedback = "y"
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
    tmpcode = []
    for i in code:
        tmpcode.append(i["Afkorting"])
    code = tmpcode
    print(code)
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n=========================================================")
        print(board)
        guess_input = input("Do een gok: ")
        try:
            guess_list = guess_input.upper().replace(" ", "").split(",")
            #print(guess_list)
            guess_response = auto_feedback(guess_list, code)
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


def pc_game(feedback):
    manual_feedback = False
    if feedback == "y":
        manual_feedback = True
    board = ""
    steps = 0
    code = input("Verzin een code: ").upper().replace(" ", "").split(",")
    while True:
        guess_list = random_guess()
        if manual_feedback:
            guess_response = man_feedback(guess_list, code)
        else:
            guess_response = auto_feedback(guess_list, code)
        steps += 1
        right_color_str = ""
        if guess_response[0] > 0:
            right_color_str = "?" * guess_response[0]
        right_place_str = ""
        if guess_response[1] > 0:
            right_place_str = "!" * guess_response[1]
        board += "{:^10} {:^10} {:^10} {:^10} || {:^10} {:^10}\n".format(guess_list[0], guess_list[1],
                                                                             guess_list[2], guess_list[3],
                                                                             right_color_str, right_place_str)
        if guess_response[1] == 4:
            print(f"WINNER WINNER CHICKEN DINNER.\nJE HEBT DE CODE GERADEN IN {steps} STAPPEN!")
            break


def random_guess():
    guess_list = []
    for i in range(0, 4):
        guess_list.append(colors[random.randint(0, 5)]["Afkorting"])
    return guess_list

def auto_feedback(guesslst, code):
    #Check if color is in code
    right_color = 0
    right_place = 0
    for g, color in enumerate(guesslst):
        if color in code:
            if code[g] == guesslst[g]:
                right_place += 1
            else:
                right_color += 1
    return right_color, right_place

def man_feedback(guesslst, code):
    while True:
        try:
            print(guesslst)
            right_color = int(input("Hoeveel zitten in de code maar niet op de juiste plek? "))
            right_place = int(input("Hoeveel zitten op de juiste plek en hebben de juiste waarde? "))
            if auto_feedback(guesslst, code) != (right_color, right_place):
                raise Exception
            else:
                return right_color, right_place
        except ValueError:
            print("Geef geldige waarde")
        except Exception:
             print("De feedback die je geeft is niet juist!")



# def set_code(code):
#     code.clear()
#     code_global = code
#     # for i in code:
#     #     code_global.append(i["Afkorting"])
#     print("Code is set!")
#     print(code_global)

def explain():
    for c in colors:
        print(f'{c["Kleur"]} = {c["Afkorting"]}')



def game():
    explain()
    settings = menu()
    if settings[0] == "y":
        player_game()
    if settings[0] == "n":
        pc_game(settings[1])


game()
