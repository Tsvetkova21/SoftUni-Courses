number_of_student = int(input())
student_data = {}
for _ in range(number_of_student):
    students_name, grade = input().split(' ')
    if students_name not in student_data:
        student_data[students_name] = []
    student_data[students_name].append(float(grade))

for student, grades in student_data.items():
    convert_grades_to_string = ' '. join(map(lambda grade: f'{grade:.2f}', grades))
    average_grade = sum(grades)/len(grades)
    print(f'{student} -> {convert_grades_to_string} (avg: {average_grade:.2f})')
