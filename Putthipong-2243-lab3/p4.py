'''
Putthipong Phukhansung
633040224-3
'''

vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]


string = str(input("Enter a string input: "))
string_up = list(map(str.upper, string))
check = [each for each in string_up if each in vowels]


print("chare are", list(string))
print(f"The entered stgring is {string} and the result if convert a vowel to uppercase are :\n", list(check))