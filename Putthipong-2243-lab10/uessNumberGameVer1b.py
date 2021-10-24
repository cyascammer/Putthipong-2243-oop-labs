from random import randint


class GuessNumberGameVer1:
    # class attribute
    _numOfGames = 0

    def __init__(self, minNum=1, maxNum=10, maxTries=3):
        self._minNum = minNum
        self._maxNum = maxNum
        self._maxTries = maxTries
        GuessNumberGameVer1.updateNumOfGames()

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
        
        i = self._maxTries

        while True:
            guess = input(f"Please enter a guess ({self._minNum}, {self._maxNum}):")
            i -= 1
            print(f"Guess is {guess}")
            if int(guess) == answer:
                print(f"Congratulations! That's correct")
                break
            elif i == 0:
                print(f"Sorry, please keep trying")
                break


if __name__ == "__main__":
    gng1 = GuessNumberGameVer1()
    # print(gng1)
    gng2 = GuessNumberGameVer1(5, 8)
    # print(gng2)
    # print(f"The current number of games is {GuessNumberGameVer1.getNumOfGames()}")
    gng3 = GuessNumberGameVer1(5, 8, 2)
    print(gng3)
    print(f"The current number of games is {GuessNumberGameVer1.getNumOfGames()}")
    gng3.playGame()