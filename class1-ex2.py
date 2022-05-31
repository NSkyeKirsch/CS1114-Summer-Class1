sum = 0
num_grades = -1
grade = 0
while grade != 'Q':
    sum += int(grade)
    num_grades += 1
    grade = input("Enter a grade or Q to quit: ")

print("The sum is: {}".format(sum) if num_grades > 0 else "You didn't enter any data!")
print("The average is: {}".format(sum/num_grades) if num_grades > 0 else "")



