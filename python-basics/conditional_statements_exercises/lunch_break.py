name_of_serial = input()
episode_duration = int(input())
duration_rest = int(input())
from math import ceil

time_for_lunch = duration_rest / 8
time_for_rest = duration_rest / 4

passed_time = duration_rest - time_for_lunch - time_for_rest
remaining_time = abs(passed_time - episode_duration)


if passed_time >= episode_duration:
    print(f"You have enough time to watch {name_of_serial} and left with {ceil(remaining_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_serial}, you need {ceil(remaining_time)} more minutes.")