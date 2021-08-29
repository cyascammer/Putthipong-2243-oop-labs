'''
Puttthipong Phukhansung
633040224-3
'''

def Check_Vowel(string, vowels):
    check = [each for each in string if each in vowels]
    print(f'Vowels in Hello world are {check}')


if __name__ == '__main__':
    string = str(input("Enter string input : "))
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
    Check_Vowel(string, vowels)
