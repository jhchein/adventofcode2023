import re
import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

def gear_product(row_num, col_num):
    nearby_numbers = [
        number[3]
        for number in numbers 
        if (row_num - 1 <= number[0] <= row_num + 1) and (number[1] - 1 <= col_num <= number[2] + 1)
    ]
    if len(nearby_numbers) == 2:
        return np.prod(nearby_numbers)
    else:
        return 0

numbers = [
    (row_num, match.start(), match.end() - 1, int(match.group()))
    for row_num, line in enumerate(data)
    for match in re.finditer(r"\d+", line)
]

total = sum([
    gear_product(row_num, start)
    for row_num, line in enumerate(data)
    for start, symbol in enumerate(line)
    if symbol == "*"
])

print(total)
