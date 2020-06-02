fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for x in line:
        if not x in lst:
            lst.append(x)
        else:
            continue
lst.sort()
print(lst)
