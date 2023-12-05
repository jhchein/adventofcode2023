import re
from math import prod

# Regular expressions
num_color = re.compile(r"(\d+) (\w+)")

# Maximum cubes
max_cubes = {"red": 12, "green": 13, "blue": 14}

# Read input
with open("input.txt") as f:
    games = f.read().splitlines()

max_products = [
    prod(
        max(
            int(amount) if color == cube_color else 0
            for amount, color in num_color.findall(game)
        )
        for cube_color in max_cubes
    )
    for game in games
]

print(f"Part 2: The sum of all valid game IDs is {sum(max_products)}.")
