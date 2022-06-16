# Calculate if target is prime using a 'for' loop

import math

target = int(input("Enter a positive integer, target: "))

sqrt_target = math.sqrt(target)
sqrt_target_floor = math.floor(sqrt_target)
isPrime = True

for divisor in range(2, sqrt_target_floor + 1):
    if target % divisor == 0:
        isPrime = False
        break

print(target, 'is prime:', isPrime)
