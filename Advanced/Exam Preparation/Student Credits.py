def students_credits(*students_credit):
    Diyan_courses={}
    all_earned_credits = 0
    needed_credits = 240
    result = []
    for courses in students_credit:
        curr_course = courses.split("-")
        course, credit, max_points, points = curr_course[0], int(curr_course[1]),int(curr_course[2]), int(curr_course[3])
        earned_credit=points/max_points*credit
        if course not in Diyan_courses:
            Diyan_courses[course]=0
        Diyan_courses[course]+=earned_credit
        all_earned_credits+=earned_credit

    if needed_credits>all_earned_credits:
        result.append(f"Diyan needs {(needed_credits-all_earned_credits):.1f} credits more for a diploma.")
    else:
        result.append(f"Diyan gets a diploma with {all_earned_credits:.1f} credits.")

    sorted_dian_points_info = sorted(Diyan_courses.items(), key=lambda a: -a[1])

    for course_cc in sorted_dian_points_info:
        course, point = course_cc[0], course_cc[1]
        result.append(f"{course} - {point:.1f}")
    return '\n'.join(result)


print(
    students_credits(
            "Python Development-15-200-200",
            "JavaScript Development-12-500-480",
            "C++ Development-30-500-405",
            "Java Development-10-300-150"
        )
    )


