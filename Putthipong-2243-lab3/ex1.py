'''
Putthipong Phukhansung
633040224-3
'''

import random

def Random_n():
    global n
    min_num = 1
    max_num = 10
    n = random.randint(min_num, max_num)
    return n

def guess_number():
    guess_num = int(input("Enter an integer to guess: "))
    i = 0
    round_to_guess = 4

    while guess_num != n and round_to_guess >= 0:

        if guess_num < n:
            print("Try a higher number.")
            print("You have",round_to_guess,"guesses remaining")
            guess_num = int(input("Enter an integer to guess: "))
            i += 1
            round_to_guess -= 1
        elif guess_num > n:
            print("Try a lower number.")
            print("You have",round_to_guess,"guesses remaining")
            guess_num = int(input("Enter an integer to guess: "))
            i += 1
            round_to_guess -= 1

    if guess_num == n:
            print("Congrats that you guess the number correctly")


if __name__ == "__main__":
    Random_n()
    guess_number()