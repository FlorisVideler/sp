import feedback as fb
import ast
import random

# Basicly just do a random guess, pretty easy
def random_guess(colors):
    guess_list = []
    for i in range(0, 4):
        guess_list.append(colors[random.randint(0, 5)]["Afkorting"])
    return guess_list


# uses the simple strategy from YET ANOTHER MASTERMIND STRATEGY by Barteld Kooi
def simple_algorithm(possible_combis, feedback, guess):
    print(len(possible_combis), " left")
    new_list = []
    for i in possible_combis:
        if fb.auto_feedback(guess, i) == feedback:
            new_list.append(i)
    print(len(new_list), " after left")
    return new_list


# uses the worst case strategy from YET ANOTHER MASTERMIND STRATEGY by Barteld Kooi
def best_worstcase_algorithm(possible_combis):
    ansdict = {}
    for i in possible_combis:
        ansdict[i] = []
        for j in possible_combis:
            feedback = fb.auto_feedback(i, j)
            ansdict[i].append(feedback)
    all_highest = []
    for key in ansdict:
        # print(key)
        unilist = []
        countlist = []
        q = ansdict[key]
        for i in q:
            if i not in unilist:
                unilist.append(i)
        for i in unilist:
            countlist.append(q.count(i))
        highest = max(countlist)
        all_highest.append([key, unilist[countlist.index(highest)], highest])

    allcounts = []
    for i in all_highest:
        allcounts.append(i[2])
    lowest = min(allcounts)
    options = []
    for i in all_highest:
        if i[2] <= lowest:
            options.append(i)
    print("RETURNING ", ast.literal_eval(options[0][0]))
    print(len(options), " options left")
    return ast.literal_eval(options[0][0])


def selfmade_algorithm(possible_combis, feedback, guess):
    new_list = []
    if guess[0] and guess[1] and guess[2] == guess[3]:
        last_guesse_num = guess[0]
        if feedback == (0, 0):
            for i in possible_combis:
                if guess[0] not in i:
                    new_list.append(i)
        else:
            new_list = possible_combis
        print("INT", int(guess[0]))
        if int(guess[0]) <= 6:
            if guess in new_list:
                print("REMOVED", guess)
                new_list.remove(guess)
            new_list.insert(0, [f"{int(guess[0]) + 1}", f"{int(guess[0]) + 1}", f"{int(guess[0]) + 1}",
                                f"{int(guess[0]) + 1}"])
    else:
        new_list = possible_combis
        new_list.remove(guess)
        random.shuffle(new_list)
    return new_list
