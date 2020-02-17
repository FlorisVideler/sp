def auto_feedback(guesslst, code):
    #print(guesslst)
    #print("g", guesslst)
    # right_color = 0
    # right_place = 0
    # for g in range(0,len(guesslst)):
    #     if guesslst[g] == code[g]:
    #         right_place += 1
    #     if guesslst[g] in code:
    #         right_color += 1
    # print(right_color, right_place)
    # right_color = right_color-right_place
    # print(right_color)

    # Check if color is in code
    right_color = 0
    right_place = 0
    matched = []
    tmp_guesslst = []
    tmp_code = []
    for g in range(0, len(guesslst)):
        if guesslst[g] == code[g]:
            right_place += 1
            tmp = code[g]
            tmp_guesslst.append(tmp)
            tmp_code.append(tmp)
    guesslst2 = [x for x in guesslst if x not in tmp_guesslst]
    code2 = [x for x in code if x not in tmp_code]
    for g in range(0, len(guesslst2)):
        if guesslst2[g] in code2:
            right_color += 1
    return right_color, right_place



def manual_feedback(guesslst, code):
    while True:
        try:
            print("{:^10} {:^10} {:^10} {:^10}\n".format(guesslst[0], guesslst[1], guesslst[2], guesslst[3]))
            right_color = int(input("Hoeveel zitten in de code maar niet op de juiste plek? "))
            right_place = int(input("Hoeveel zitten op de juiste plek en hebben de juiste waarde? "))
            if auto_feedback(guesslst, code) != (right_color, right_place):
                raise Exception
            else:
                return right_color, right_place
        except ValueError:
            print("Geef geldige waarde")
        except Exception:
            print("De feedback die je geeft is niet juist! ", auto_feedback(guesslst, code))