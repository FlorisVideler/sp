# Uit deze opdracht kwam ik niet dus heb ik deze code gebruikt: https://www.programiz.com/python-programming/examples/fibonacci-recursion
# Ook na de uitleg op de website snap ik nog steeds niet echt hoe deze werkt.
# Ik zou graag wat meer oefenen met recursieve fencties


def fiboncci(n):
    if n <= 1:
        return n
    else:
        return fiboncci(n - 1) + fiboncci(n - 2)


print(fiboncci(6))
