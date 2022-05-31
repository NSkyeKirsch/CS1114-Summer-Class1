import random

rand_num = random.randint(1, 50)

guess = int(input("Enter your guess, an integer between 1 and 50: "))

while 1 <= guess <= 50:
    if guess == rand_num:
        print("You Win!")
        break
    elif guess <= rand_num:
        print("Higher!")
    else:
        print("Lower!")

    guess = int(input("Enter your guess, an integer between 1 and 50: "))

print("Goodbye.")