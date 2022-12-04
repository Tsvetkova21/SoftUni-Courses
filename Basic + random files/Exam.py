exam_hour=int(input())
exam_minute=int(input())
arrival_hour=int(input())
arrival_minute=int(input())
minutes_exam=exam_hour*60+exam_minute
minutes_arrival=arrival_hour*60+arrival_minute

if minutes_exam-30<=minutes_arrival<=minutes_exam:
    print("On time")
    earlier_arrival = minutes_exam - minutes_arrival
    if 0<earlier_arrival<=30:
        print(f'{earlier_arrival} minutes before the start')
elif minutes_exam-30>minutes_arrival:
    print("Early")
    earlier_arrival=minutes_exam-minutes_arrival
    if earlier_arrival<60:
        print(f'{earlier_arrival} minutes before the start')
    else:
        print(f'{earlier_arrival//60}:{earlier_arrival%60:02d} hours before the start')
elif minutes_arrival>minutes_exam:
    print("Late")
    late_arrival = minutes_arrival-minutes_exam
    if late_arrival<60:
        print(f'{late_arrival:02d} minutes after the start')
    else:
        print(f'{late_arrival // 60}:{late_arrival % 60:02d} hours after the start')