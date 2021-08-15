'''
Putthipong Phukhansung
633040224-3
Problem 4
'''

sum = 0
count = 0
end_input = False
while not end_input:
    n = int(input("Enter an integer:"))
    sum = sum + n
    count = count + 1
    avg = sum / count
print(f"Average is {avg}")