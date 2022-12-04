
n=int(input())
calculated_value = 0
max_weight =0
max_time=0
max_quality=0

for i in range(0,n):
    weight_snowball=int(input())
    time_needed=int(input())
    quality = int(input())

    new_calculated_value = (weight_snowball/time_needed)**quality
    if calculated_value<new_calculated_value:
        calculated_value=new_calculated_value
        max_weight = weight_snowball
        max_time = time_needed
        max_quality = quality

print(f'{max_weight} : {max_time} = {calculated_value:.0f} '
      f'({max_quality})')