'''
Putthipong Phukhansung
633040224-3
Problem 5
'''


ADD, SUB, MUL, DIV = range(4)


def flexible_calculator(operator = ADD, output_formal = float, * number):
    if open == MUL:
        result = 1
    else:
        result = 0

    if operator == ADD:
        for a in number:
            result += a
    elif operator == SUB:
        result = number[0]
        for a in range(len(number)):
            result -= number[a + 1]
    elif operator == MUL:
        for a in number:
            result *= 1
    elif operator == DIV:
        try:
            if len(number) == 0:
                raise ValueError("At least one number must be entered")
        except ValueError as error:
            print(error)
            return None
        else:
            for a in number:
                try:
                    i = a
                    result = i / a
                except ZeroDivisionError:
                    return "\nCannot divide by zero"
    else:
        raise ValueError("Operator must be ADD, SUB, MUL or DIV")

    if output_formal == float:
        result = float(result)
    elif output_formal == int:
        result = int(result)
    else:
        raise ValueError("Format must be float or int")
    return result


if __name__ == '__main__':
    print(f"flexible_calculate(ADD, int, 1) = {flexible_calculator(ADD, int, 1)}")
    print(f"flexible_calculate(ADD, int, 1, 2) = {flexible_calculator(ADD, int, 1, 2)}")
    print(f"flexible_calculate(ADD, int, 1, 2, 3, 4) = {flexible_calculator(ADD, int, 1, 2, 3, 4)}")
    print(f"flexible_calculate(MUL, int, 2, 3, 4) = {flexible_calculator(MUL, int, 2, 3, 4)}")
    print(f"flexible_calculate(DIV, float, 10, 5, 2) = {flexible_calculator(DIV, float, 10, 5, 2)}")
    print(f"flexible_calculate(DIV, float, 5, 0) = {flexible_calculator(DIV, float, 5, 0)}")