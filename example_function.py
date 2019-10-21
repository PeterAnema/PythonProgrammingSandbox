

def welkom(name):
    return "Welkom %s" % name

def repeat(s, n):
    for __ in range(n):
        print(s)


#=============================================

repeat(welkom("Peter"), 5)

repeat(welkom("Vera"), 7)

