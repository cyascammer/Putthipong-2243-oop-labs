'''
Putthipong Phukhansung
633040224-3
'''

from functools import reduce

def compute_sum_positive_odd_numbers():
    number = list(map(int, input("Enter numbers in the list:").split()))
    positive_odd = list(filter(lambda x: (x % 2 == 1 and x > 0 ), number))
    sum_positive_odd = reduce((lambda x, y: x + y), positive_odd)
    return print(sum_positive_odd)

if __name__ == '__main__':
    compute_sum_positive_odd_numbers()