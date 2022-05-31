product = 1
num = int(input("Enter a number: "))

for value in range(num, 0, -1):
    product = product * value

print(num, "factorial is", product)