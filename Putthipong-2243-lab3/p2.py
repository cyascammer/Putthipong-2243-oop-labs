'''
Putthipong Phukhansung
633040224-3
'''

fruits = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]


def upper():
    n = 1
    for item in fruits:
        print(n,". ",item.upper(),sep='')
        n += 1

def upper_sort():        
    for i in range(len(fruits)):
        fruits[i] = fruits[i].upper()
    fruits.sort()
    print(fruits)


if __name__ == '__main__':
    print("The fruits are",fruits)
    print("After converting fruits to uppercase letter, fruits are")
    upper()
    print("After sorting fruits, fruits are")
    upper_sort()