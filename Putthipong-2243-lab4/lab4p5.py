'''
Putthipong Phukhansung
633040224-3
Problem 5
'''

import logging

input_logging = False

while not input_logging:
    try:
        n1 = int(input("Enter n1:"))
        n2 = int(input("Enter n2:"))
        if n2 < 0:
            break
        result = n1 / n2
        print(f"The result is {result}")
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(f"n = {n1}")
        logging.debug(f"n = {n2}")
        break

    except NameError:
        print(" is not giving error code ")