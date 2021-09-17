'''
Putthipong Phukhansung
633040224-3
'''

import math


class Circle:
    def input_floatnum():
        global n
        try:
            n = float(input("Enter a radius:"))
        except ValueError:
            print("Please enter a valid floating-point number for the circle radius")
            exit()
        return n

    def cal_radius():
        return math.pi * pow(n, 2)

    def cal_perimeter():
        return 2 * math.pi * n


if __name__ == '__main__':
    Circle.input_floatnum()
    Circle.cal_radius()
    print(f"The circle with radius {n} has the area as {{:.2f}} and the perimater as {{:.2f}}".format(Circle.cal_radius(), Circle.cal_perimeter()))