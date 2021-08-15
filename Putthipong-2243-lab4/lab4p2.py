'''
Putthipong Phukhansung
633040224-3
Problem 2
'''

# n1 = int(input("Enter n1:"))
# n2 = int(input("Enter n2:"))
# answer = n1 + n2
# print(f'The answer of {n1} + {n2} is {answer}')

def get_float(arg):
    correct_input = False
    while not correct_input:  # this is a while loop
        try:
            number = float(input(f"Enter {arg} floating point number:"))
            return number
        except ValueError:
            print("Please enter a valid floating point number")


def get_operrator():
    n1 = get_float("the first")
    n2 = get_float("the second")
    operator = ("+", "-", "*", "/")
    input_ops = input("Please enter an operator (+,-,*,/):")

    if input_ops == "+":
        result_plus = n1 + n2
        print(f"{n1} + {n2} = {result_plus}")
    elif input_ops == "-":
        result_minus = n1 - n2
        print(f"{n1} - {n2} = {result_minus}")
    elif input_ops == "*":
        result_multiply = n1 * n2
        print(f"{n1} * {n2} = {result_multiply}")
    elif input_ops == "/":
        try:
            n1 / n2
        except ZeroDivisionError:
            print("Cannot divide by zero")
            exit()
        result_divide = n1 / n2
        print(f"{n1} / {n2} = {result_divide}") 
    elif input_ops != operator:
        print("Unknow operator")


if __name__ == "__main__":
    get_operrator()