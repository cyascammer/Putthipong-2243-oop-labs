'''
Putthipong Phukhansung
633040224-3
Problem 4
'''


def get_float(arg):
    while True:

        try:
            num = input(f"Please enter the {arg} operand ('q' to quit): ")
            if num == "q" or num == 'Q':
                return num
            num = float(num)
            if num != float(num):
                raise Exception
            return num
        except:
            print("Please enter floating point number.")


def robust_calculator():
    global n1
    global n2

    while True:
        n1 = get_float("first ")
        if n1 == 'q'or n1 == 'Q':
            break
        n2 = get_float("second ")
        if n2 == "q" or n2 == "Q":
            break
        
        calculator()


def calculator():

    try:
        input_operator = input("please enter an operator (+,-,*,/)")
        if input_operator not in "(+, -, *, /)":
            print("Operation must be ADD, SUB, MUL or DIV.")
        elif input_operator == "+":
            result = n1 + n2                
        elif input_operator == "-":
            result = n1 - n2                
        elif input_operator == "*":
            result = n1 * n2                
        elif input_operator == "/":
            result = n1 / n2                
        else:
            result = "Unknow opreator"
    except ZeroDivisionError:
        print("Cannot divide by zero ")


    if input_operator  in ('+','-','*','/'):
        math = input("Enter out format (float, int): ")
        if math == 'float':
            result = float(result)
            print(result)
        if math == 'int':
            result = int(result)
            print(result)



if __name__=="__main__":
    robust_calculator()