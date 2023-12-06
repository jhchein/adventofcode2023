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
time = int("".join(lines[0].split(": ")[1].split()))
distance = int("".join(lines[1].split(": ")[1].split()))

print(get_valid_combinations(time, distance))
