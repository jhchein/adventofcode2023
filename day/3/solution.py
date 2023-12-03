import re
import numpy as np

with open("input.txt", "r") as f:
    data = f.read().splitlines()


def part_1(data):
    mask = np.array([[symbol not in "0123456789." for symbol in line] for line in data])

    numbers = [
        (row_num, match.start(), match.end() - 1, match.group())
        for row_num, line in enumerate(data)
        for match in re.finditer(r"\d+", line)
    ]

    sum = 0
    for number in numbers:
        row_num, start, end, value = number

        nearby_mask = mask[
            max(row_num - 1, 0) : min(row_num + 2, len(mask)),
            max(start - 1, 0) : min(end + 2, len(mask[0])),
        ]

        if nearby_mask.any():
            print(f"Found number {value} at position {row_num, start, end}")
            sum += int(value)
    print(sum)


if __name__ == "__main__":
    part_1(data)
