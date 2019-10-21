from math import *

def plot(punten):
    """Dit is mijn functie voor iets
    :param punten list of 2 element tuples
    :return None
    """
    for p in punten:
        print("*"*int(p[1]*30+30))

f = lambda x: sin(x)

#----------------------------------------------------------
# Main

punten = [(x*0.1, f(x*0.1)) for x in range(0,100)]

plot(punten)
