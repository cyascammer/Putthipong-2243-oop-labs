'''
Puttthipong Phukhansung
633040224-3
'''

student_id = int(input("Enter your student ID : "))

while True:
    try:
        midterm_score = float(input("Enter the student's midterm exam mark (0-100) : "))
        if midterm_score <= 100 and midterm_score >= 0:
            break
        elif midterm_score <= 0 or midterm_score >= 100:
            print("Enter a score in rage[0,100]")
    except ValueError:
        print("Enter a score as a decimal number.")

Midterm = (midterm_score * 40/100)

while True:
    try:
        final_score = float(input("Enter the student's midterm exam mark (0-100) : "))
        if final_score  <= 100 and final_score  >= 0:
            break
        elif final_score  <= 0 or final_score >= 100:
            print("Enter a score in rage[0,100]")
    except ValueError:
        print("Enter a score as a decimal number.")

Finalterm = (final_score * 60/100)
totelscore = Finalterm + Midterm

if totelscore >= 80 and totelscore <= 100:
    getgrade = 'A'
elif totelscore >= 70 and totelscore <= 80:
    getgrade = 'B'
elif totelscore >= 60 and totelscore <= 70:
    getgrade = 'C'
elif totelscore >= 50 and totelscore <= 60:
    getgrade = 'D'
else:
    getgrade = 'F'


print(f'Student ID {student_id} has the total mark as{totelscore} and has grade as {getgrade}')