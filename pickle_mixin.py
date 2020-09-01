import os
import pickle

class PickleMixin:

    __EXTENSION = '.pickle'

    def __init__(self, *args, **kwargs):
        pass

    def save_to_pickle(self, filename = None):
        if filename is None:
            filename = type(self).__name__ + PickleMixin.__EXTENSION

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except:
            print('Cannot write pickle to file %s' % filename)


    def update_from_pickle(self, filename = None):
        if filename is None:
            filename = type(self).__name__ + PickleMixin.__EXTENSION

        try:
            with open(filename, 'rb') as f:
                self.__dict__.update(pickle.load(f).__dict__)
        except:
            print('Cannot read pickle from file %s' % filename)


class Persoon(PickleMixin):

    def __init__(self, name):
        super().__init__(name)
        self._name = name

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Persoon("%s")' % self._name


class Student(PickleMixin, Persoon):

    def __init__(self, name):
        super().__init__(name)


#-----------

# p1 = Persoon('Peter')
# print(p1)
#
# p1.save_to_pickle()

p2 = Persoon('')
p2.update_from_pickle()

print(p2)