largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print("Invalid input")
    if largest == None:
        largest = n
    elif largest < n:
        largest = n
    else:
        if smallest == None:
            smallest = n
        elif smallest > n:
            smallest = n
print("Maximum is", largest)
print("Minimum is", smallest)
