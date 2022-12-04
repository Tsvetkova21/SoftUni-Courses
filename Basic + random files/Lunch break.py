import math

serial=input()
episode_duration=int(input())
pause_duration=int(input())
lunch_duration=0.125*pause_duration
rest_duration=0.25*pause_duration

time_for_episode=pause_duration-lunch_duration-rest_duration

if episode_duration<=time_for_episode:

    print(f'You have enough time to watch {serial} and'
          f' left with {math.ceil(time_for_episode-episode_duration)}'
          f' minutes free time.')

else:
    print(f"You don't have enough time to watch {serial},"
          f" you need {math.ceil(episode_duration-time_for_episode)}"
          f" more minutes.")
