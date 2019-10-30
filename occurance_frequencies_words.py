import re

#tekst="Mijn benen worden als vanzelf naar het bankje getrokken, heerlijk warm bij het brandend kampvuur. Vermoeid strek ik mijn benen en sluit mijn ogen. Mijn hoofd is zo vol met woorden, ze struikelen gewoon over elkaar. Rustig maar meisje, je bent vandaag vrij, laat het los heeft je werkgever je toch gezegd. Jij draagt niet alleen de verantwoording. Het voelt wel zo, die verantwoording neem ik mezelf op de hals, ik weet het maar al te goed. Het zit gewoon in me, zorgen voor anderen, dat geeft me juist een fijn gevoel. Als ik geen verantwoording draag voel ik me leeg van binnen, dan val ik in slaap en word ik lui. Jaren geleden heb ik dat gemerkt, bij mijn burn-out, ik kwam nergens meer toe, had nergens zin in, kwam liever ook niet buiten, zelfs lezen was nog te vermoeiend, slapen kon ik ook niet. Het enige wat ik wilde was wat domme spelletjes spelen op de pc. Uit verveling typte ik wat in bij google en kwam op de site van libelle, zag dat er een forum was en begon wat te lezen. Eerst interesseerde het me niet, tot ik een topic vond waar meerdere schreven over hun gevoel van moeheid. Plots was ik aan het meepraten en zo zat ik nachtenlang met iemand op het forum, die ook niet kon slapen, we hadden steun aan elkaar en vonden in elkaar herkenning. Mijn man kwam een keer naar beneden en vroeg met wie ik aan het chatten was, ik chat niet zei ik, maar ik praat op een forum met een andere vrouw van mijn leeftijd. Laat me nu maar. Na enkele maanden kroop ik uit het dal der tranen en besefte dat ik zo niet leven wilde. De baan die ik had kon me niet meer boeien en nam ontslag. Nu voelde ik me bevrijd."

with open('kampvuur.txt') as f:
    tekst = f.read().rstrip('\n').lower()

tekst = re.sub('[^a-z\s]', ' ', tekst)

words = tekst.split()
unique_words = set(words)

d = dict()
for word in unique_words:
    d[word] = words.count(word)

print(d)

print("Number of words %d" % len(words))
print("Number of unique words %d" % len(unique_words))
print()

# for word, n in d.items():
#    print("%-20s %3d %s" % (word, n, "*" * n))

# ## of ...
# ##
for word, n in sorted(d.items(), key = lambda item: item[1], reverse = True):
    print("%-20s: %s %d" % (word, "\u2588" * n, n))

# ## of ...
# ##
# from operator import itemgetter
# for word, n in sorted(d.items(), key = itemgetter(1), reverse = True):
#    print("%-20s: %s %d" % (word, "\u2588" * n, n))
