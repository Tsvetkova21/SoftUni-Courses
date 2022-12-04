persons = int(input())
capacity = int(input())
left = persons%capacity
if left>capacity:
    courses=persons // capacity+int(left/capacity)
elif left == 0:
    courses = persons // capacity
else:
    courses = persons // capacity+1
print(courses)