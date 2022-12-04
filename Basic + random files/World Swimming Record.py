import math

record_sec=float(input())
lenght_m=float(input())
time_sec_1m_swimming=float(input())
slow=math.floor(lenght_m/15)
all_time=lenght_m*time_sec_1m_swimming+slow*12.5
if all_time<record_sec:
    print(f" Yes, he succeeded! The new world record "
          f"is {all_time:.2f} seconds.")
else:
    not_enough=all_time-record_sec
    print(f'No, he failed! He was {not_enough:.2f} '
          f'seconds slower.')
