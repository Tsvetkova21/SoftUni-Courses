count_unsatf_grade = int(input())
grade = 0
task = " "
failed_times = 0
sum_grades = 0
solved_task = 0
has_failed = False
last_problem = ' '

while failed_times < count_unsatf_grade:
    last_problem = task
    task = input()
    if task == "Enough":
        has_failed = True
        break
    grade = int(input())

    if grade <= 4:
        failed_times += 1

    if failed_times == count_unsatf_grade:
        break
    sum_grades +=grade
    solved_task +=1
    last_problem = task

if  not has_failed:
    print(f'You need a break, {count_unsatf_grade} poor grades.')

else:
    print(f"Average score: {(sum_grades / solved_task):.2f}")
    print(f'Number of problems: {solved_task}')
    print(f'Last problem: {last_problem}')