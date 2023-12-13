import numpy as np
from itertools import combinations

with open("example1.txt", "r") as file:
    lines = file.readlines()

board = np.array([list(line.strip()) for line in lines])

# Find empty rows and columns
empty_rows = np.all(board == ".", axis=1)
empty_cols = np.all(board == ".", axis=0)

# Find all galaxy positions
galaxy_positions = [
    (y, x)
    for y, row in enumerate(board, start=1)
    for x, char in enumerate(row)
    if char == "#"
]

# Calculate the total shortest distance between all galaxy positions
total = sum(
    abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    for pos1, pos2 in combinations(galaxy_positions, 2)
)
print(f"Total: {total}")