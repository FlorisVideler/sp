def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:  # Deelbaar door 3 & 5
            output = "fizzbuzz"
        elif i % 3 == 0:  # Deelbaar door 3
            output = "fizz"
        elif i % 5 == 0:  # Deelbaar door 5
            output = "buz"
        else:
            output = i
        print(output)


fizzbuzz()
