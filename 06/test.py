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

test_1 = get_valid_combinations(7, 9)
print(f"Test 1: {test_1}")
assert test_1 == 4, f"Test 1 failed: {test_1}"

test_2 = get_valid_combinations(15, 40)
print(f"Test 2: {test_2}")
assert test_2 == 8, f"Test 2 failed: {test_2}"

test_3 = get_valid_combinations(30, 200)
print(f"Test 3: {test_3}")
assert test_3 == 9, f"Test 3 failed: {test_3}"