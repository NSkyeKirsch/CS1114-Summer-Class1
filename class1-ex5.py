stu_num = input("Enter a student number or Q to quit: ")

while stu_num != 'Q' and stu_num != 'q':
    num_grades = 3
    sum = 0
    while num_grades > 0:  # iterates 3x per student
        sum += int(input("Enter a grade: "))
        num_grades -= 1

    print("Student num: {} //// Avg: {}".format(stu_num, sum/3))

    stu_num = input("Enter a student number or Q to quit: ")