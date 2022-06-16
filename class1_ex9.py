print(" "*3, end='')
for header in range(1, 6):
    print(' '*4, header, sep='', end='')
print()
print("-"*28)

for row in range(1, 6):
    print(row, ' |', sep='', end='')  # outer loop (row number)

    for col in range(1, 6):  # inner loop
        if row*col < 10:
            print(' '*4, row * col, sep='', end='')
        else:
            print(' '*3, row * col, sep='', end='')
    print()
