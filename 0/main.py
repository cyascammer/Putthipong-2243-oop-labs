# Putthipong Phukhansung 633040224-3

def compute_avg_list(n):
    number = input("Enter %d positive numbers:"%n).split()
    num = list(map(float,number))
    print("Numbers are",end=" ")
    print(list(number))
    average = sum(num)/n
    return average
    
if _name_ == '_main_':
    average = computer_avg_list(5)
    print("The total sum is %.1f"%average)
    average = computer_avg_list(3)
    print("The total sum is %.1f"%average)

