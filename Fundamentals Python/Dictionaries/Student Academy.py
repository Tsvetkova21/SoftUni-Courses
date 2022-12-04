lines = int(input())
counter = 0
sum = 0
average_grade = 0
students = {}

for i in range(lines):
    student = input()
    grade = input()
    if student not in students:
        students[student]=[]
    students[student].append(float(grade))

for key,value in students.items():
    counter = len(value)
    for value in students[key]:
        sum +=value
    average_grade=sum/counter
    if average_grade>=4.50:
        print(f"{key} -> {(sum/counter):.2f}")
    counter = 0
    sum = 0

