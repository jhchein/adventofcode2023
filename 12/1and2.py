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
        springs = "?".join(
            [spring for spring in springs.split() for _ in range(multiplier)]
        )
        target = ",".join([t for t in target.split(",") for _ in range(multiplier)])

    solution_counter = process_combination_dp(springs, target)

    # If the solution is present, check if it matches the given solution
    if solution_counter and solution:
        print(
            f"{'Correct' if solution_counter == int(solution) else 'Wrong'} solution: {solution_counter} != {solution}"
        )
    elif solution_counter is None:
        print("No solution found")

    return solution_counter


def main(filename, multiplier=1):
    lines = load_file(filename)
    total = sum(process_line(line, multiplier=multiplier) for line in tqdm(lines))
    print(total)


if __name__ == "__main__":
    # sys.argv[1] = filename (example.txt for part 1, example2.txt for part 2, input.txt for the solution)
    # sys.argv[2] = multiplier (1 for part 1, 5 for part 2)
    main(sys.argv[1], int(sys.argv[2]))


# 815364548481 !
