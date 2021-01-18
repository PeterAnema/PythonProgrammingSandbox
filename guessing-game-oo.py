import demo_random
import sys

class GuessingGame:

    def __init__(self, low = 1, high = 99):
        self.__low = low
        self.__high = high
        self.__magic_number = demo_random.randint(low, high)
        self.__number_of_guesses = 0

    def guess(self, guess):
        self.__number_of_guesses += 1
        if guess > self.__magic_number:
            return 1    # is larger => lower
        elif guess < self.__magic_number:
            return -1   # is smaller => higher
        elif guess == self.__magic_number:
            return 0

    def get_number_of_guesses(self):
        return self.__number_of_guesses


class PlayGuessingGame:

    def __init__(self, low=1, high=99):
        self._low = low
        self._high = high
        self.__game = GuessingGame(low, high)

    def guess_input(self):
        return int(input("What is your next guess? "))

    def play(self):

        print("Guess a number between %d and %d" % (self._low, self._high))
        while True:
            myGuess = self.guess_input()

            result = self.__game.guess(myGuess);

            if result == 1:
                print("lower ...")
            elif result == -1:
                print("higher ...")
            elif result == 0:
                print("YEAAAH! You guessed it in {} guesses".format(self.__game.get_number_of_guesses()))
                break


class AutoPlayGuessingGame:

    def __init__(self, low = 1, high = 99, verbose = True):
        self._low = low
        self._high = high
        self.__game = GuessingGame(low, high)
        self.__verbose = verbose

    def guess(self):
        return self._low + (self._high - self._low) // 2

    def play(self):

        while True:
            myGuess = self.guess()
            if self.__verbose: print(myGuess)
            
            result = self.__game.guess(myGuess);

            if result == 1:
                self._high = myGuess - 1
            elif result == -1:
                self._low = myGuess + 1
            elif result == 0:
                if self.__verbose: print("YEAAAH! You guessed it in {} guesses".format(self.__game.get_number_of_guesses()))
                break

            # if self._highest_possible_number == self._lowest_possible_number:
            #     if self.__verbose: print("You cheated! I quit!")
            #     sys.exit()

        return self.__game.get_number_of_guesses();


class AutoPlayGuessingGameRandom(AutoPlayGuessingGame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def guess(self):
        return demo_random.randint(self._low, self._high)


# ----------------------------------------------------------

def simulation(number_of_games = 3000, auto_play = AutoPlayGuessingGame):

    number_of_guesses_counter = dict()
    for i in range(number_of_games):

        game = auto_play(verbose = False)
        # game = AutoPlayGuessingGame(verbose = False)
        # game = AutoPlayGuessingGameRandom(verbose = False)

        number_of_guesses = game.play()
        number_of_guesses_counter[number_of_guesses] = number_of_guesses_counter.get(number_of_guesses, 0) + 1

    for guess, freq in sorted(number_of_guesses_counter.items(), key=lambda item: item[0]):
        freqperc = freq / number_of_games * 100
        print("%3d %s %.1f%%" % (guess, "\u2588" * int(freqperc), freqperc))


if __name__ == '__main__':

    # game = PlayGuessingGame()

    # game = AutoPlayGuessingGame()
    # game = AutoPlayGuessingGameRandom()

    # game.play()


    #simulation()
    simulation(auto_play = AutoPlayGuessingGame)
    # simulation(auto_play = AutoPlayGuessingGameRandom)
