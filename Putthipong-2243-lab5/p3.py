'''
Putthipong Phukhansung
633040224-3
Problem 3
'''


def recur_factorial():
    if n == 1:
        return n
    else:
        return n * recur_factorial(n-1)
        

while True:
    try:
        number = int(input("Enter a positive integer:"))
        if number <= 0:
            print("Please enter an interger that is non-negative")
            break
        elif number == 0:
            print("The factorial of 0 is 1")
            break
        else:
            print("The factorial of ", number, "is", recur_factorial(number))        
    except ValueError:
        print("Please enter a valid imteger")
        break