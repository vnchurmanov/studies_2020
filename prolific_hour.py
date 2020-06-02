name = input("Enter file:")
fh = open(name)
counts = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split(":")
    x = words[0]
    hour = x[-2:]
    counts[hour] = counts.get(hour, 0) + 1
lst = sorted([(k, v) for k, v in counts.items()])
for x, y in lst:
    print(x, y)