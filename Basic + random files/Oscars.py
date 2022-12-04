actor_name = input()
points_academy = float(input())
count_evaluators = int(input())
sum_points=points_academy
for num in range(0,count_evaluators):
    name_evaluator=input()
    points=float(input())
    sum_points+=points*len(name_evaluator)/2
    if sum_points>=1250.5:
        print(f"Congratulations, {actor_name} "
              f"got a nominee for leading role with {sum_points:.1f}!")
        exit()
print(f"Sorry, {actor_name} you need "
      f"{(1250.5-sum_points):.1f} more!")

