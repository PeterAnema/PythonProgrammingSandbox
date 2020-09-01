import re

# with open('kampvuur.txt') as f:
#     s = f.read().rstrip('\n')

# s = "Mijn benen worden als vanzelf naar het bankje getrokken, heerlijk warm bij het brandend kampvuur. Vermoeid strek ik mijn benen en sluit mijn ogen. Mijn hoofd is zo vol met woorden, ze struikelen gewoon over elkaar. Rustig maar meisje, je bent vandaag vrij, laat het los heeft je werkgever je toch gezegd. Jij draagt niet alleen de verantwoording. Het voelt wel zo, die verantwoording neem ik mezelf op de hals, ik weet het maar al te goed. Het zit gewoon in me, zorgen voor anderen, dat geeft me juist een fijn gevoel. Als ik geen verantwoording draag voel ik me leeg van binnen, dan val ik in slaap en word ik lui. Jaren geleden heb ik dat gemerkt, bij mijn burn-out, ik kwam nergens meer toe, had nergens zin in, kwam liever ook niet buiten, zelfs lezen was nog te vermoeiend, slapen kon ik ook niet. Het enige wat ik wilde was wat domme spelletjes spelen op de pc. Uit verveling typte ik wat in bij google en kwam op de site van libelle, zag dat er een forum was en begon wat te lezen. Eerst interesseerde het me niet, tot ik een topic vond waar meerdere schreven over hun gevoel van moeheid. Plots was ik aan het meepraten en zo zat ik nachtenlang met iemand op het forum, die ook niet kon slapen, we hadden steun aan elkaar en vonden in elkaar herkenning. Mijn man kwam een keer naar beneden en vroeg met wie ik aan het chatten was, ik chat niet zei ik, maar ik praat op een forum met een andere vrouw van mijn leeftijd. Laat me nu maar. Na enkele maanden kroop ik uit het dal der tranen en besefte dat ik zo niet leven wilde. De baan die ik had kon me niet meer boeien en nam ontslag. Nu voelde ik me bevrijd."

s = """Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28]
Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[29]
Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.
The Python 2 language, i.e. Python 2.7.x, was officially discontinued on 1 January 2020 (first planned for 2015) after which security patches and other improvements will not be released for it.[30][31] With Python 2's end-of-life, only Python 3.5.x[32] and later are supported."""

# s = s.lower().\
#     replace('.', ' ').\
#     replace(',', ' ').\
#     replace('!', ' ').\
#     replace('?', ' ').\
#     replace('(', ' ').\
#     replace(')', ' ').\
#     replace('[', ' ').\
#     replace(']', ' ')

## or
# s = s.lower().translate(str.maketrans('', '', '.,!?()[]'))

## or
s = re.sub('[^a-z\s]', ' ', s.lower())

words = s.split()
unique_words = set(words)

d = dict()
for word in sorted(unique_words):
    if not word.isdecimal():
        d[word] = words.count(word)


# print(d)

## or
##
# d = {}
# for word in words:
#     d[word] = d.get(word, 0) + 1


# ## or
# ##
# d = {word: words.count(word) for word in sorted(unique_words)}

print("Number of words %d" % len(words))
print("Number of unique words %d" % len(unique_words))
print()

# for word, n in d.items():
#    print(f'{word}: {n}')

## or ...
##
# for word, n in d.items():
#    print(f'{word:20} {n:3} {"*" * n}')

## or ...
##
for word, n in sorted(d.items(), key = lambda item: item[1], reverse = True):
    block_character = '\u2588'
    print('%-20s: %s %d' % (word, block_character * n, n))
    # print(f'{word:20} {n:3} {block_character * n}')

# ## or ...
# ##
# from operator import itemgetter
# for word, n in sorted(d.items(), key = itemgetter(1), reverse = True):
#    print("%-20s: %s %d" % (word, "\u2588" * n, n))
