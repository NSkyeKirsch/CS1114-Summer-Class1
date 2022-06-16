count = 0
alpha = 0

while (count < 100):  # 0, 1, 2... 99
    if count % 5 == 0:  # count 0, 5, 10, 15, 20... 90, 95
        alpha += 1
    else:
        alpha += 2
    count += 1

print(alpha)
