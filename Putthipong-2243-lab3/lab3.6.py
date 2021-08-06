'''
Putthipong Phukhansung
633040224-3
'''

from functools import reduce

def sum_of_the_square():
    number = []
    get_num = int(input("Enter an integer: "))
    [number.append(i) for i in range(1, get_num + 1)]
    square = list(map(lambda x: x * x, number))
    sum_square = reduce(lambda x, y: x + y, square)
    return print(f"The sum of the square of {number} is {sum_square} ")


if __name__ == '__main__':
    sum_of_the_square()