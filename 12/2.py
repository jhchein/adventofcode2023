import sys
import re
from tqdm import tqdm
from dp import process_combination_dp

# Compile the regular expressions
spring_target_solution_re = re.compile(r"([\.#?]+) ([0-9,]+)(?: - (\d+))?")
variable_position_re = re.compile("\?")
consecutive_hash_re = re.compile("#+")

def load_file(filename):
    with open(filename, "r") as file:
        return file.readlines()

def process_line(line, multiplier=1):
    # Get the springs and target, the solution is not always present
    springs, target, solution = spring_target_solution_re.findall(line)[0]

    if multiplier > 1:
        springs = "?".join(springs.split()* multiplier)
        target = ",".join(target.split(",") * multiplier)

    solution_counter = process_combination_dp(springs, target)

    # If the solution is present, check if it matches the given solution
    if solution_counter and solution:
        print(f"Correct solution: {solution_counter} == {solution}" if solution_counter == int(solution) else f"Wrong solution: {solution_counter} != {solution}")
    elif not solution:
        pass
    else:
        print("No solution found")

    return solution_counter

def main(filename, multiplier=1):
    lines = load_file(filename)
    total = sum(process_line(line, multiplier=multiplier) for line in tqdm(lines))
    print(total)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))

# 815364548481 !