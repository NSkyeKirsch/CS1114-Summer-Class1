value = int(input("Enter an integer greater than 0: "))

while value > 0:
    if value % 2 == 0:
        print("{} is evenly divisible by 2.".format(value))
    else:
        print("{} is not evenly divisible by 2.".format(value))
    value -= 1
