import re
from itertools import cycle
from math import gcd
from functools import reduce

map_pattern = re.compile(r"([1-9A-Z]{3}) = \(([1-9A-Z]{3}), ([1-9A-Z]{3})\)")

with open("input.txt", "r") as f:
    lines = f.readlines()

desert_map = {node: {"L": left, "R": right} for line in lines[1:] for node, left, right in map_pattern.findall(line)}
left_right_instructions = cycle(lines[0].strip())

steps = 0
current_nodes = [node for node in desert_map.keys() if node[-1] == "A"]
print(f"Starting at {current_nodes}")

Z_encounters = {i: [] for i, _ in enumerate(current_nodes)}

while not all(node[-1] == "Z" for node in current_nodes):
    instruction = next(left_right_instructions)
    current_nodes = [desert_map[node][instruction] for node in current_nodes]
    steps += 1

    for i, node in enumerate(current_nodes):
        if node[-1] == "Z":
            Z_encounters[i].append(steps)

            # If all nodes have encountered Z, we check the cycles of each node.
            # We can then calculate the Least Common Multiple of all cycles
            # to find the number of steps required to reach the end of the desert.
            if all(len(encounters) > 1 for encounters in Z_encounters.values()):
                cycles = [reduce(gcd, [encounters[i] - encounters[i-1] for i in range(1, len(encounters))]) for encounters in Z_encounters.values()]
                print(f"Cycles: {cycles}")
                print(f"LCM: {reduce(lambda x, y: x * y // gcd(x, y), cycles)}")
                exit()
            
print(f"Reached the end of the desert after {steps} steps.")