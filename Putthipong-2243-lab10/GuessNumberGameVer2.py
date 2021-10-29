from GuessNumberGameVer1.py import GuessNumberGameVer1
from random import randint


class GuessNumberGameVer2(GuessNumberGameVer1):
    # class attribute
    _numOfGames = 0

    def __init__(self, *args, **kwargs):
        super(GuessNumberGameVer2, self).__init__(*args, **kwargs)
        self._guesses = []
        self._numGuesses = 0
        GuessNumberGameVer2.updateNumOfGames()

    @classmethod
    def updateNumOfGames(cls):
        cls._numOfGames = cls._numOfGames + 1

    @classmethod
    def getNumOfGames(cls):
        return cls._numOfGames

    def __str__(self):
        return f"Guess number game:({self._minNum}, {self._maxNum}, {self._maxTries})"

    def playGame(self):
        answer = randint(self._minNum, self._maxNum)
        print(f"Answer is {answer}")
        print(f"GuessNumberGame with min number as {self._minNum}, max number as {self._maxNum}, max num of tries as {self._maxTries}")

        gngl.playGame()

        while True:
            print(f"If want to play again? type 'y' to continue or 'q' to quit:")
            get_input_2 = input(f"Type 'a' to see all your guesses or 'g' to see a guess on a sspecific play:")

            if get_input_2 == 'y':
                self._guess.clear()
                numTries = self._maxTrise
                gngl.playGames()
                break
            elif get_input_2 == 'q':
                exit()
            elif get_input_2 == 'a':
                gngl.showGGuesses()
            elif get_input_2 == 'g':
                gngl.showSpecific()
            else:
                pass


            maxTries = maxTries - 1
            guess = randint(self._minNum, self._maxNum)
            # print(f"Guess is {guess}")
            if int(guess) == answer:
                print(f"Congratulations! That's correct")
                break            
            elif self._maxTries == 0:
                if int(guess) < answer:
                    print(f"Please type a higher number! The number of remain tries is {self._maxTries}")
                elif int(guess) > answer:
                    print(f"Please type a lower number! The number of remain tries is {self._maxTries}")
                print(f"Sorry, please keep trying")
                break
            elif int(guess) < answer:
                print(f"Please type a higher number! The number of remain tries is {self._maxTries}")
            elif int(guess) > answer:
                print(f"Please type a lower number! The number of remain tries is {self._maxTries}")  


if __name__ == "__main__":
    gngl = GuessNumberGameVer2(5, 6, 1)
    # print(gng)
    gngl.playGames()
    print("Now let's play only one game")
    gngl.playGame()