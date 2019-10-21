import os
import sys
import json
import pickle

#-------------------------------------------------------------------

class UserAbstract:
    __FILENAME = ''

    def __init__(self):
        self.name = ""
        self.age = 0
        self.height = 0
        self.weight = 0
        if self.store_exists():
            self.load_from_store()

    def display(self):
        print('\nUser Information:')
        print('User Name  :', self.name)
        print('User Age   :', self.age)
        print('User Height:', self.height)
        print('User Weight:', self.weight)

    def load_from_input(self):
        self.name = input('\nEnter User Name: ')
        self.age = int(input('Enter Age: '))
        self.height = int(input('Enter Height: '))
        self.weight = int(input('Enter Weight: '))

    @classmethod
    def store_exists(cls):
        raise NotImplementedError("Please Implement this method")

    def save_to_store(self):
        raise NotImplementedError("Please Implement this method")

    def load_from_store(self):
        raise NotImplementedError("Please Implement this method")

#-------------------------------------------------------------------

class UserInFile(UserAbstract):
    __FILENAME = 'user.txt'

    @classmethod
    def store_exists(cls):
        return os.path.isfile(UserInFile.__FILENAME)

    def save_to_store(self):
        self.save_to_file()

    def load_from_store(self):
        self.load_from_file()

    def save_to_file(self):
        with open(UserInFile.__FILENAME,'w') as f:
            f.write(self.name + '\n')
            f.write(str(self.age) + '\n')
            f.write(str(self.height) + '\n')
            f.write(str(self.weight) + '\n')

    def load_from_file(self):
        with open(UserInFile.__FILENAME) as f:
            self.name = f.readline().strip();
            self.age = int(f.readline().strip());
            self.height = int(f.readline().strip());
            self.weight = int(f.readline().strip());

#-------------------------------------------------------------------

class UserInJson(UserAbstract):
    __FILENAME = 'user.json'

    @classmethod
    def store_exists(cls):
        return os.path.isfile(UserInJson.__FILENAME)

    def save_to_store(self):
        self.save_to_json()

    def load_from_store(self):
        self.load_from_json()

    def save_to_json(self):
        with open(UserInJson.__FILENAME, 'wb') as f:
            s = json.dumps(self.__dict__, ensure_ascii = False).encode()
            f.write(s)

    def load_from_json(self):
        with open(UserInJson.__FILENAME, 'rb') as f:
            s = f.read().decode()
            self.__dict__.update(json.loads(s))

#-------------------------------------------------------------------

class UserInPickle(UserAbstract):
    __FILENAME = 'user.pickle'

    @classmethod
    def store_exists(cls):
        return os.path.isfile(UserInPickle.__FILENAME)

    def save_to_store(self):
        self.save_to_pickle()

    def load_from_store(self):
        self.load_from_pickle()

    def save_to_pickle(self):
        with open(UserInPickle.__FILENAME, 'wb') as f:
            pickle.dump(self, f)

    def load_from_pickle(self):
        with open(UserInPickle.__FILENAME, 'rb') as f:
            self.__dict__.update(pickle.load(f).__dict__)


#-------------------------------------------------------------------

#User = UserInFile
#User = UserInJson
User = UserInPickle

#-------------------------------------------------------------------

if __name__ == '__main__':

    user = User()
    user.display()

    while True:
        response = input("\nEnter new user details? [Y/N]: ").upper()
        if response != 'Y': break

        user.load_from_input()
        user.save_to_store()

        user.display()
