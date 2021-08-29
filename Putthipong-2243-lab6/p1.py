filenames1 = (2, 123.4567, 10000, 12345.67)
filenames2 = []

for t in filenames1:
    filename = "file_00{:.0f}".format(t)
    filenames2.append(filename)


print(str(filenames2[0]), "{:.2f}, {:1.2e}, {:1.2e}"
.format(filenames1[1], filenames1[2], filenames1[3]))