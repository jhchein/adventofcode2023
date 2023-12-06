import re
import numpy as np

def find_min(a, b):
    low = 1
    high = a
    while low < high:
        mid = (low + high) // 2
        if mid * (a - mid) > b:
            high = mid
        else:
            low = mid + 1
    return low


def get_valid_combinations(time, distance):
    max_speed, remainder = divmod(time, 2)
    min_speed = find_min(time, distance)
    return 2 * (max_speed - min_speed) + 1 + remainder

with open("input.txt", "r") as f:
    lines = f.readlines()
time_and_distance = [tuple(map(int, re.findall(r"\d+", line))) for line in lines]
races = list(zip(*time_and_distance))

print(np.prod([get_valid_combinations(race[0], race[1]) for race in races]))
    