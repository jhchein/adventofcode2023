import re
from math import prod

# Regular expressions
game_id = re.compile(r"Game (\d+):")
num_color = re.compile(r"(\d+) (\w+)")

# Maximum cubes
max_cubes = {"red": 12, "green": 13, "blue": 14}

# Read input
with open("input.txt") as f:
    games = f.read().splitlines()

valid_game_ids = [
    int(game_id.search(game).group(1))
    for game in games
    if all(int(amount) <= max_cubes[color] for amount, color in num_color.findall(game))
]

print(f"Part 1: The sum of all valid game IDs is {sum(valid_game_ids)}.")