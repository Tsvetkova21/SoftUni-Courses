name = input()
grades = 0
sum_grades = 0.0
excluded_count = 0
grade_class = 0.0

while True:

    grade_class= float(input())
    grades += 1
    if grade_class < 4.00:
        excluded_count+=1

        if excluded_count ==2:
            print (f'{name} has been excluded at {grades} grade')
            break
        grades -= 1

    else:
        sum_grades += grade_class

    if grades == 12:
        print (f'{name} graduated. Average grade: {(sum_grades/(grades)):.2f} ')
        break