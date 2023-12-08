import re
from itertools import cycle
from math import gcd
from functools import reduce

with open("input.txt", "r") as f:
    lines = f.readlines()

map_pattern = re.compile(r"([1-9A-Z]{3}) = \(([1-9A-Z]{3}), ([1-9A-Z]{3})\)")
desert_map = {node: {"L": left, "R": right} for line in lines[1:] for node, left, right in map_pattern.findall(line)}
starting_nodes = [node for node in desert_map.keys() if node[-1] == "A"]

def get_z_encounters(node):
    left_right_instructions = cycle(lines[0].strip())
    steps = 0
    Z_encounters = []
    while len(Z_encounters) < 2:
        instruction = next(left_right_instructions)
        node = desert_map[node][instruction]
        steps += 1
        if node[-1] == "Z":
            Z_encounters.append(steps)
    return Z_encounters

cycles = [Z_encounters[1] - Z_encounters[0] for starting_node in starting_nodes for Z_encounters in [get_z_encounters(starting_node)]]

# If all nodes have encountered Z, we check the cycles of each node.
# We can then calculate the Least Common Multiple of all cycles
# to find the number of steps required to reach the end of the desert.
print(f"Cycles: {cycles}")
print(f"LCM: {reduce(lambda x, y: x * y // gcd(x, y), cycles)}")
