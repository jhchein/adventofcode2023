import re

with open("input.txt") as f:
    input = f.read().splitlines()

# schema
# Game 1: 1 red, 3 blue, 11 green; 1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green

game_id = re.compile(r"Game (\d+):")
num_color = re.compile(r"(\d+) (\w+)")

# 12 red cubes, 13 green cubes, and 14 blue cubes
max_cubes = {"red": 12, "green": 13, "blue": 14}

### PART 1 ###
sum = 0
for game in input:
    print(f"Cube distribution: {game}")
    id = game_id.search(game).group(1)

    for draw in num_color.findall(game):
        amount, color = draw
        # print(f"Found {amount} {color} cubes.")
        if int(amount) > max_cubes[color]:
            print(f"Game {id} is invalid, because there are too many {color} cubes.")

            print("Skipping to next game.")
            break
    else:
        print(f"Game {id} is valid.")
        sum += int(id)

print(f" Part 1: The sum of all valid game IDs is {sum}.")


### PART 2 ###

sum = 0
for game in input:
    max_values = {"red": 0, "green": 0, "blue": 0}
    for draw in num_color.findall(game):
        amount, color = draw
        max_values[color] = max(max_values[color], int(amount))
    # multiply all max values
    max_product = 1
    for color in max_values:
        max_product *= max_values[color]
    print(f"Game {game_id.search(game).group(1)}: {max_product}")
    sum += max_product

print(f" Part 2: The sum of all valid game IDs is {sum}.")
