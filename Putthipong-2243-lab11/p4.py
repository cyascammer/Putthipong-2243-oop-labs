#Putthipong Phukhansung 633040224-3
"""
Write a program to open a CSV file with the name “numbers.csv” that writes three columns of numbers. Then the program reads the data from file “numbers.csv” and writes out the data to a new CSV file with the name “numbers2.csv”, swapping around the first and third columns.  Then the program adds the fourth column which contains the average of the first three.  Finally, the program writes each row on the console and writes each row to the file “numbers2.csv”
After you run the program, two files (“numbers.csv” and “numbers2.csv”) are generated automatically.
"""
import csv


with open("numbers.csv", "w", newline="") as fw:
    w = csv.writer(fw)
    w.writerow([2, 4, 6])
    w.writerow([3, 7, 5])
    w.writerow([8, 9, 7])

with open("numbers.csv", "r") as f:
    with open("numbers2.csv", "w", newline="") as fw2:
        rows = csv.reader(f)
        w2 = csv.writer(fw2)
        for row in rows:
            row[0], row[2] = row[2], row[0]
            number = (float(row[0]) + float(row[1]) + float(row[2])) / len(row)
            row.append(number)
            w2.writerow(row)

with open("numbers2.csv", "r") as r:
    lines = csv.reader(r)
    for line in lines :
        print(line)