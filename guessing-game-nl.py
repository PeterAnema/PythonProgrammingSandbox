import demo_random

print("Raad een getal tussen 1 en 99")

geheim_getal = demo_random.randint(1, 99)

aantal_pogingen = 0
while True:

    gok = int(input("Wat is jouw volgende gok? "))
    aantal_pogingen += 1

    if gok > geheim_getal:
        print("lager ...")

    elif gok < geheim_getal:
        print("hoger ...")

    elif gok == geheim_getal:
        print("JAAA! Goed geraden in %d pogingen" % aantal_pogingen)
        break
