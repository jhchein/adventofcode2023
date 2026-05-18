import sys
import itertools

def load_file(filename):
    with open(filename, "r") as file:
        return file.readlines()
    
import numpy as np

def create_puzzles(lines):
    puzzles = []
    puzzle = []
    for line in lines:
        if line == "\n":
            puzzles.append(np.array(puzzle))
            puzzle = []
        else:
            puzzle.append(list(line.strip()))
    puzzles.append(np.array(puzzle))
    return puzzles
    # return [np.array(list(g)) for k, g in itertools.groupby(lines, key=lambda x: x == "\n") if not k]

def find_mirror_row(puzzle):
    # The puzzle is symmetrical above and below the mirror row
    results = []
    for i in range(1, puzzle.shape[0]):
        top = puzzle[:i]
        bottom = puzzle[i:]
        mirrored_bottom = np.flip(bottom, axis=0)
        # print(f"i: {i}")
        # print(f"top:\n{top}")
        # print(f"bottom:\n{bottom}")
        # make sure they are remove the starting lines of top or the last line of bottom so that they are the same size
        if top.shape[0] > mirrored_bottom.shape[0]:
            top = top[-mirrored_bottom.shape[0]:]
        elif top.shape[0] < mirrored_bottom.shape[0]:
            mirrored_bottom = mirrored_bottom[:top.shape[0]]
            
        # print(f"top:\n{top}")
        # print(f"mirrored_bottom:\n{mirrored_bottom}")
        if np.array_equal(top, mirrored_bottom):
            results.append(i)
    return results

# def find_mirror_row(puzzle):
#     # The puzzle is symmetrical above and below the mirror row
#     # Use numpy functionality to find the mirror row
#     return [i for i in range(2, puzzle.shape[0]-1) if np.array_equal(puzzle[:i][-min(i, puzzle.shape[0]-i):], np.flip(puzzle[i:], axis=0)[:min(i, puzzle.shape[0]-i)])]

def find_mirror_column(puzzle):
    results = []
    for i in range(1, puzzle.shape[1]):
        left = puzzle[:, :i]
        right = puzzle[:, i:]
        mirrored_right = np.flip(right, axis=1)
        # print(f"i: {i}")
        # print(f"left:\n{left}")
        # print(f"right:\n{right}")
        # make sure they are remove the starting lines of top or the last line of bottom so that they are the same size
        if left.shape[1] > mirrored_right.shape[1]:
            left = left[:, -mirrored_right.shape[1]:]
        elif left.shape[1] < mirrored_right.shape[1]:
            mirrored_right = mirrored_right[:, :left.shape[1]]
            
        # print(f"left:\n{left}")
        # print(f"mirrored_right:\n{mirrored_right}")
        if np.array_equal(left, mirrored_right):
            results.append(i)
    return results

def main(filename):
    lines = load_file(filename)
    puzzles = create_puzzles(lines)
    score = 0
    for i, puzzle in enumerate(puzzles):
        # print(f"puzzle:\n{puzzle}")
        mirror_row = find_mirror_row(puzzle)
        if mirror_row:
            print(f"{i}: mirror_row: {mirror_row[0]} of {puzzle.shape[0]}")
            score += mirror_row[0] * 100
        elif mirror_column := find_mirror_column(puzzle):
            print(f"{i}: mirror_column: {mirror_column[0]} of {puzzle.shape[1]}")
            score += mirror_column[0]
        else:
            print(f"{i}: No mirror found")
            print(f"puzzle:\n{puzzle}")
    print(score)


if __name__ == '__main__':
    # sys.argv[1] = filename (example.txt for part 1, example2.txt for part 2, input.txt for the solution)
    main(sys.argv[1])

# 18641 too low
# 26310 ?