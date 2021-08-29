'''
Putthipong Phukhansung 
633040224-3
'''

def compute_avg():
    List_num = []
    total = 0
    while True :
        n = int(input("Enter a positive number:"))
        if n <= 0 :
            break
        List_num.append(n)
        total += 1

    for i in range(len(List_num)):
        List_num[i] = float(List_num[i])
    print("Numbers are", List_num)
    sm = sum(List_num)
    avg = sm/total
    print("The average number of the list is",'%.1f' %avg)


if __name__ == '__main__':
    compute_avg()