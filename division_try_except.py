while True:

    try:
        inp = input("What's your favourite number? ")
        num = int(inp)
        print("Thanks, your favourite number is %d" % num)
        break

    except ValueError:
        print("Eek, that's not valid a number!")
