
class Zoo:

    def __init__(self):
        self.animals = ['dog', 'cat', 'bird', 'fish', 'horse']
        self.index = 0

    def append(self, animal):
        self.animals.append(animal)

    def __next__(self):
        try:
            animal = self.animals[self.index]
            self.index += 1
            return animal
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        self.index = 0
        return self


if __name__ == '__main__':

    zoo = Zoo()
    zoo.append('lion')

    for animal in zoo:
        print(animal)

    for animal in zoo:
        print(animal)