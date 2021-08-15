'''
Putthipong Phukhansung
633040224-3
Problem 6
'''

def sum_of_list(numbers):
    return sum(numbers)


def average(sum, n):
    # ZeroDivisionError if list is empty
    return sum / n


def final_data(data):
    try:
        for item in data:
            print("Average:", average(sum_of_list(item), len(item)))
    except ZeroDivisionError:
        print("Thelist iss empty")

list1 = [10, 20, 30, 40, 50]
list2 = [100, 200, 300, 400, 500]
# empty list
list3 = []
lists = [list1, list2, list3]
final_data(lists)