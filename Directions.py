def dirReduc(direct):
    x = list()
    for i in direct:
        if i == 'NORTH':
            x.append(1)
        elif i == 'SOUTH':
            x.append(3)
        elif i == 'EAST':
            x.append(10)
        else:
            x.append(12)
    b = 0
    e = 2
    for i in range(len(x)):
        double = x[b:e]
        if len(x) > 1 and len(double) > 1:
            second = double[1]
            if double[0] - second == 2 or double[0] - second == -2:
                x.pop(b)
                x.pop(e - 2)
                if b != 0 and e != 2:
                    b -= 1
                    e -= 1
            else:
                b += 1
                e += 1
    result = []
    for i in x:
        if i == 1:
            result.append("NORTH")
        elif i == 3:
            result.append("SOUTH")
        elif i == 10:
            result.append("EAST")
        else:
            result.append("WEST")
    return result
