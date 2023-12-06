from math import sqrt, ceil, floor

with open("input.txt", "r") as f:
    lines = f.readlines()
time = int("".join(lines[0].split(": ")[1].split()))
distance = int("".join(lines[1].split(": ")[1].split()))

# See README.md for explanation
p = -time
q = distance

t_moving_max = floor(-p/2 + sqrt((p/2)**2 - q))
t_moving_min = ceil(-p/2 - sqrt((p/2)**2 - q))

values = t_moving_max - t_moving_min + 1
print(values)