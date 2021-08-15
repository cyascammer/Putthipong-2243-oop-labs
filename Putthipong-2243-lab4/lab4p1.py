'''
Putthipong Phukhansung
633040224-3
Problem 1
'''

patients = [[70, 1.80], [58, 1.55], [100, 1.90]]


def calculate_bmi(_weight, _height):
    return _weight / (_height * 2)


i = 0
for patient in patients:
    weight, height = patients[0]
    bmi = calculate_bmi(weight, height)
    i += 1
    print(f"Patient's BMI is: {bmi:0.02f}")