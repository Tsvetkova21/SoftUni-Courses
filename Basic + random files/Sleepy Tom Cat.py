holidays=int(input())
work_days=365-holidays
time_to_play=work_days*63+holidays*127
if time_to_play>30000:
    print('Tom will run away')
    print(f'{(time_to_play-30000)//60} hours '
          f'and {(time_to_play-30000)%60} minutes more for play')
if time_to_play<=30000:
    print('Tom sleeps well')
    print(f'{(30000-time_to_play) // 60} hours '
          f'and {(30000-time_to_play) % 60} minutes less for play')
