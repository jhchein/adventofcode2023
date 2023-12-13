import sys
import re
from tqdm import tqdm

# Compile the regular expressions
spring_target_solution_re = re.compile(r"([\.#?]+) ([0-9,]+)(?: - (\d+))?")
variable_position_re = re.compile("\?")
consecutive_hash_re = re.compile("#+")

def load_file(filename):
    with open(filename, "r") as file:
        return file.readlines()

def process_line(line):
    # Get the springs and target, the solution is not always present
    springs, target, solution = spring_target_solution_re.findall(line)[0]

    # Retrieves the variable positions ("?") within the springs
    variable_positions = [match.start() for match in variable_position_re.finditer(springs)]

    # Goes through all the possible combinations of "#" and "." for the missing positions
    solution_counter = sum(
        1 for i in range(2**len(variable_positions))
        if process_combination(i, springs, target, variable_positions)
    )

    # If the solution is present, check if it matches the given solution
    if solution_counter and solution:
        print("Correct solution" if solution_counter == int(solution) else "Wrong solution")
    elif not solution:
        pass
    else:
        print("No solution found")

    return solution_counter

def process_combination(i, springs, target, variable_positions):
    # Converts the index to a binary string and pads it with zeros
    binary = bin(i)[2:].zfill(len(variable_positions))
    # Create an iterator over the binary string
    binary_iter = iter(binary)

    # Replace each "?" in springs with the next character from binary
    springs_ = re.sub("\?", lambda x: next(binary_iter), springs)

    # Replace each 0 with "." and each 1 with "#"
    springs_ = springs_.replace("0", ".").replace("1", "#")

    # Finds consecutive groups of "#" and compares them to the goal
    consecutive = [len(match.group()) for match in consecutive_hash_re.finditer(springs_)]

    return consecutive == list(map(int, target.split(",")))

def main(filename):
    lines = load_file(filename)
    total = sum(process_line(line) for line in tqdm(lines))
    print(total)

if __name__ == '__main__':
    main(sys.argv[1])