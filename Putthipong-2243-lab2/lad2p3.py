'''
Puttthipong Phukhansung
633040224-3
'''

list1 = [1, 2, 3, 4, 5]


def add_number_to_list():
    global list1, list2
    print("Before adding an interger, the list is", list1)
    add_list = int(input("Enter a number to add to a list:"))
    list1.append(add_list)
    print("After adding an integer", add_list, ", thelist is", list1)

def replace_number_in_list():
    print("Finding a number to replace in the list", list1)
    find_list = int(input("Enter a number to find:"))
    replace_list = int(input("Enter a new number to replace:"))
    list2 = [x if x != find_list else replace_list for x in list1]
    print("After replace", find_list, "with",replace_list, ", the new list is", list2)

def remove_number_in_list():
    print("Finding a number to remove in the list", list1)
    remove_list = int(input("Enter a number to remove:"))
    list1.remove(remove_list)
    print("After removing", remove_list, ", the list is", list1)


if __name__ == 'main':
    add_number_to_list()
    replace_number_in_list()
    remove_number_in_list()
