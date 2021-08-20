'''
Putthipong Phukhansung
633040224-3
problem 1
'''

import math


def hypotenuse(n1, n2):
    print("Sqrt({}^2 + {}^2) = {}".format(n1,n2,math.sqrt(pow(n1,2) + pow(n2,2))))

hypotenuse(3.0,4.0)
hypotenuse(3,4)
hypotenuse(3,4.0)