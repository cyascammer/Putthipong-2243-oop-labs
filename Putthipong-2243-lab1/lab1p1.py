'''
Putthipong Phukhansung 
633040224-3
'''

import random

def compute_avg_list(n):
    number = input("Enter %d positive number: " %n)
    print("You entered", number)
    u_list = number.split()
    print("Numbers are ", u_list)

    for i in range(len(u_list)):
        u_list[i] = int(u_list[i])     
    
    avg = sum(u_list) / len(u_list)

    print("The average number of the list is", avg)

def compute_avg():
    list = []
    while True:
        number2 = float(input("Enter a positive number: "))
        if number2 > 0:
            break
        else:
            list.append()
        total_avg = sum(list) / len(list)
        print("number are {list}")
        print("The average number of the list is {total_avg}")

def test_compute_avg_list():
    min_number = 1
    max_number = 10
    n = random.randint(min_number, max_number)
    compute_avg_list(n)


if __name__ == '__main__':
    test_compute_avg_list()