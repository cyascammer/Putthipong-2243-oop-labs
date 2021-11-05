#Putthipong Phukhansung 633040224-3

import sys

try:
    num_args = len(sys.argv)
    operand1 = sys.argv[1]
    if operand1 == 'q' or open == 'Q':
        print("program is quits...")
    elif num_args != 4:
        print("<operatoe> <operand1> <operand2>")
    elif operand1 == '+':
        operand2 = float(sys.argv[2])
        operand3 = float(sys.argv[3])
        args_plus  = operand2 + operand3
        print(f"{operand2} + {operand3} is {args_plus}")
    elif operand1 == '-':
        operand2 = float(sys.argv[2])
        operand3 = float(sys.argv[3])
        args_minus  = operand2 - operand3
        print(f"{operand2} - {operand3} is {args_minus}")
    elif operand1 == '*':
        operand2 = float(sys.argv[2])
        operand3 = float(sys.argv[3])
        args_multiply  = operand2 * operand3
        print(f"{operand2} * {operand3} is {args_multiply}")
    elif operand1 == '/':
        try:
            operand2 = float(sys.argv[2])
            operand3 = float(sys.argv[3])
            args_divide  = operand2 / operand3
            print(f"{operand2} / {operand3} is {args_divide}")
        except ZeroDivisionError:
            print(f"{operand2} cannot be divide by {operand3}")

except ValueError:
    print("Operands are invalid. They are not numbers")

    