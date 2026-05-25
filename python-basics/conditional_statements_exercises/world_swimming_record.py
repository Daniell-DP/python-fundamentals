record_in_second = float(input())
distance_in_meters = float(input())
time_in_second_distance_one_meter = float(input())
from math import floor

time_in_second = distance_in_meters * time_in_second_distance_one_meter

delay = floor(distance_in_meters / 15) * 12.5

all_time = time_in_second + delay

if all_time < record_in_second:
    print(f"Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
else:
    missing_time = abs(all_time - record_in_second)
    print(f"No, he failed! He was {missing_time:.2f} seconds slower.")