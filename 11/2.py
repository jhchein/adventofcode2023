import numpy as np
from itertools import combinations

with open("input.txt", "r") as file:
    board = np.array([list(line.strip()) for line in file])

def find_empty_indices(board, axis):
    return np.where(np.all(board == ".", axis=axis))[0]

empty_row_indices = find_empty_indices(board, axis=1)
empty_col_indices = find_empty_indices(board, axis=0)

def calculate_distance(pos1, pos2, factor=1_000_000):
    """ Calculates the distance between two positions. """
    (x_min, x_max), (y_min, y_max) = sorted((pos1[0], pos2[0])), sorted((pos1[1], pos2[1]))
    
    # We could cache this, but hey, it's fast enough
    empty_row_between = len([index for index in empty_row_indices if x_min < index < x_max])
    empty_col_between = len([index for index in empty_col_indices if y_min < index < y_max])
    
    expanded_distance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + (empty_col_between + empty_row_between) * (factor - 1)
    return expanded_distance

total = sum(
    calculate_distance(pos1, pos2)
    for pos1, pos2 in combinations(
        [(y, x) for y, row in enumerate(board) for x, char in enumerate(row) if char == "#"], 
        2
    )
)
print(f"Total: {total}")