import re

numbers_pattern = re.compile(r"(-?\d+)")

def predict_next_value(line):
    if not line or all(i == 0 for i in line):
        return 0

    next_line = [b - a for a, b in zip(line, line[1:])]
    return line[-1] + predict_next_value(next_line)

with open("input.txt", "r") as file:
    lines = file.readlines()

total = sum(predict_next_value([int(i) for i in numbers_pattern.findall(line)]) for line in lines)

print(total)
# 1938731307
# Total time: 0.028724 s
