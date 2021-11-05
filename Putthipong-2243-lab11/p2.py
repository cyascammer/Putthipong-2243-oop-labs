#Putthipong Phukhansung 633040224-3

import re

def split_str(arg):
    for data in arg:
        data_list = (re.split(' ', data))
        name = data_list[0]
        email = data_list[1]
        phone = data_list[2]
        print(f"{name} has email as {email} and phone as {phone}")
    

if __name__ == '__main__':
    lst = ["mana mana@kku,ac,th 043-222-3333",
    "manee manee@kkumail.ac.th 043-888-9999"]
    split_str(lst)
