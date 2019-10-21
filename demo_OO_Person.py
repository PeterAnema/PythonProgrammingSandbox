
class Person(object):

    __slots__ = ['name', 'residence', 'age']

    def __init__(self, name, residence, age):
        self.name = name
        self.residence = residence
        self.age = age
        
    def __str__(self):
        return "I am %s and I live in %s and I'm %d years old" % (self.name,
                                                                  self.residence,
                                                                  self.age)

    def __repr__(self):
        return "Person('%s', '%s', '%d')" % (self.name,
                                             self.residence,
                                             self.age)

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age
    
    def __ge__(self, other):
        return self.age >= other.age
    
    def __le__(self, other):
        return self.age <= other.age


class Client(Person):

    def __init__(self, name, residence, age, clientnr):
        super().__init__(name, residence, age)
        self.clientnr = clientnr

    def __str__(self):
        return "My clientnumber is %s" % self.clientnr

# ------------------

people = []
people.append( Person("Peter", "Amstelveen",62) )
people.append( Person("Peter", "Amstelveen",65) )
people.append( Person("Petra", "Amstelveen", 61) )

for p in sorted(people, key = lambda e: e.name):
    print(p)
