import re
import itertools

map_pattern = re.compile(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)")

with open("input.txt", "r") as f:
    lines = f.readlines()

desert_map = {node: {"L": left, "R": right} for line in lines[1:] for node, left, right in map_pattern.findall(line)}
left_right_instructions = itertools.cycle(instruction for instruction in lines[0].strip())

steps = 0
current_node = "AAA"

while current_node != "ZZZ":
    instruction = next(left_right_instructions)
    current_node = desert_map[current_node][instruction]
    steps += 1

print(f"Reached the end of the desert after {steps} steps.")
