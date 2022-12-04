count_student = int(input())
grade_student = 0
fail = 0
grade_3 = 0
grade_4 = 0
grade_excelent =0
grades = 0

for num in range (0, count_student):
    grade_student = float(input())
    if 2<=grade_student<=2.99:
        fail +=1
    if 3.00<=grade_student<=3.99:
        grade_3+=1
    if 4.00<=grade_student<=4.99:
        grade_4+=1
    if grade_student>= 5.00:
        grade_excelent +=1
    grades+=grade_student

print(f'Top students: {(grade_excelent/count_student*100):.2f}%')
print(f'Between 4.00 and 4.99: {(grade_4/count_student*100):.2f}%')
print(f'Between 3.00 and 3.99: {(grade_3/count_student*100):.2f}%')
print(f'Fail: {(fail/count_student*100):.2f}%')
print(f'Average: {(grades/count_student):.2f}')