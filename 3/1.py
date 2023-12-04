import re
import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()

mask = np.array([[symbol not in "0123456789." for symbol in line] for line in data])

numbers = [
    (row_num, match.start(), match.end() - 1, int(match.group()))
    for row_num, line in enumerate(data)
    for match in re.finditer(r"\d+", line)
]

total = sum(
    int(value)
    for row_num, start, end, value in numbers
    for nearby_mask in [mask[
        max(row_num - 1, 0) : min(row_num + 2, len(mask)),
        max(start - 1, 0) : min(end + 2, len(mask[0])),
    ]]
    if nearby_mask.any()
)

print(total)