import re
name = input("Enter file:")
fh = open(name)
result = 0
count = 0
for line in fh:
    n = re.findall('[0-9]+', line)
    if len(n)>2:
        x = line.split()
        for i in x:
            try:
                m = int(i)
                result += m
                count += 1
            except:
                continue
    else:
        for i in n:
            c = int(i)
            result += c
            count += 1
print(result, count)






