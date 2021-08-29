'''
Putthipong Phukhansung
633040224-3
'''

def check():
    string = str(input("Enter a string : "))
    vowels = {"A", "a", "E", "e", "I", "i", "O", "o", "U", "u"}
    lenString = [each for each in string if each in string]
    check_vewel = [each for each in string if each in vowels]
    print(f"chare are {lenString}")
    print(f"The entered string is {string} and the resuit of convert a vowel to uppercase is")
    for i in range(len(check_vewel)):
        check_vewel[i] = check_vewel[i].upper()
    print(check_vewel)


if __name__ == '__main__':
    check()
