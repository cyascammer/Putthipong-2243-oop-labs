class GuessNumberGameVer3:
    # class attribute
    _numOfGames = 0

    def __init__(self, minNum = 1, maxNum = 10, maxTries = 3):
        self._minNum = minNum
        self._maxNum = maxNum
        self._maxTries = maxTries
        GuessNumberGameVer3.updateNumOfGames()

    @classmethod
    def updateNumOfGames(cls):
        cls._numOfGames = cls._numOfGames + 1

    @classmethod
    def getNumOfGames(cls):
        return cls._numOfGames

    def __str__(self):
        return f"Guess number game:({self._minNum}, {self._maxNum}, {self._maxTries})"


if __name__ == "__main__":
    gngl = GuessNumberGameVer3(5, 6, 1)
    gngl.playGames()
    print("Now let's play only one game")
    gngl.playGame()