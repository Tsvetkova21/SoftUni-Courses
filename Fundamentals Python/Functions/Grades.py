grade_data=float(input())
def grades(grade):
    if grade >= 2.00 and grade <= 2.99 :
        return 'Fail'
    elif grade >= 3.00 and grade <= 3.49:
        return 'Poor'
    elif grade >= 3.5 and grade <=4.49:
        return 'Good'
    elif grade >= 4.5 and grade <=5.49:
        return 'Very Good'
    elif grade >= 5.5 and grade <= 6:
        return 'Excellent'
print(grades(grade_data))
