'''
Puttthipong Phukhansung
633040224-3
'''

while True:
    temp_cel = input("Enter a tamperature in Celsius: ")

    try:
        temp_cel = float(temp_cel)
    
    except:
        print("Please enter a valid floating point for the temperature.")
        continue
    else:
        break


temp_fah = ((9 * temp_cel) / 5 + 32)
print(temp_cel, "in Celsius is", temp_fah, "Fahrenheit")