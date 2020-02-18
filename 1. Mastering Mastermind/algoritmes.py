#
#
# def random_guess(colors):
#     guess_list = []
#     for i in range(0, 4):
#         guess_list.append(colors[random.randint(0, 5)]["Afkorting"])
#     return guess_list
#
#
# def simple_algortime(possible_combis, feedback, guess):
#     print(len(possible_combis), " left")
#     new_list = []
#     for i in possible_combis:
#         if mastermind.auto_feedback(guess, i) == feedback:
#             new_list.append(i)
#     print(len(new_list), " after left")
#     return new_list
#
# def best_worstcase_algortime(possible_combis):
#     ansdict = {}
#     for i in possible_combis:
#         ansdict[f"{i}"] = []
#         for j in possible_combis:
#             fb = auto_feedback(i, j)
#             ansdict[f"{i}"].append(fb)
#     allhighest = []
#     for key in ansdict:
#         #print(key)
#         unilist = []
#         countlist = []
#         q = ansdict[f"{key}"]
#         for i in q:
#             if i not in unilist:
#                 unilist.append(i)
#         for i in unilist:
#             countlist.append(q.count(i))
#         highest = max(countlist)
#         allhighest.append([key, unilist[countlist.index(highest)], highest])
#
#     allcounts = []
#     for i in allhighest:
#         allcounts.append(i[2])
#     lowest = min(allcounts)
#     options = []
#     for i in allhighest:
#         if i[2] <= lowest:
#             options.append(i)
#     print("RETURNING ", ast.literal_eval(options[0][0]))
#     print(len(options), " options left")
#     return ast.literal_eval(options[0][0])
#
#
# def selfmade_algortime(possible_combis, feedback, guess):
#     new_list = []
#     if guess[0] and guess[1] and guess[2] == guess[3]:
#         lastguessnum = guess[0]
#         if feedback == (0,0):
#             for i in possible_combis:
#                 if guess[0] not in i:
#                     new_list.append(i)
#         else:
#             new_list = possible_combis
#         print("INT", int(guess[0]))
#         if int(guess[0]) <= 6:
#             if guess in new_list:
#                 print("REMOVED", guess)
#                 new_list.remove(guess)
#             new_list.insert(0, [f"{int(guess[0])+1}", f"{int(guess[0])+1}", f"{int(guess[0])+1}", f"{int(guess[0])+1}"])
#     else:
#         new_list = possible_combis
#         new_list.remove(guess)
#         random.shuffle(new_list)
#     return new_list