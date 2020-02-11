def menu():
    print("Welkom to mastermind!")
    gives_feedback = "n"
    while True:
        who_is_playing = input("Raadt de speler? (y/n) ")
        if who_is_playing.lower() == "y":
            break
        elif who_is_playing.lower() == "n":
            gives_feedback = input("Geeft de pc feedback? (y/n) ")
            if gives_feedback.


menu()
