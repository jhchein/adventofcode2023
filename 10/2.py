from math import ceil

with open("input.txt", "r") as file:
    lines = file.readlines()

connecting_nodes = {
    "S": [(0, 1), (1, 0), (0, -1), (-1, 0)], 
    "-": [(1, 0), (-1, 0)], 
    "|": [(0, 1), (0, -1)], 
    "L": [(0, -1), (1, 0)], 
    "J": [(0, -1), (-1, 0)], 
    "7": [(0, 1), (-1, 0)], 
    "F": [(0, 1), (1, 0)], 
}

x_max = len(lines[0])-1
y_max = len(lines)-1

board = {
    (x, y): [(x+dx, y+dy) for dx, dy in connecting_nodes[char] if 0 <= x+dx <= x_max and 0 <= y+dy <= y_max]
    for y, line in enumerate(lines)
    for x, char in enumerate(line.strip())
    if char != "."
}

start = next((coord for coord, neighbors in board.items() if "S" in lines[coord[1]][coord[0]]), None)
board[start] = [neighbor for neighbor in board[start] if start in board.get(neighbor, [])]

chain = []

count = 0
prev, current = start, board[start][0]
chain.append(current)
chain.append(start)

while True:
    count += 1
    board[current].remove(prev)
    next = [neighbor for neighbor in board[current] if neighbor != prev][0]
    prev, current = current, next
    chain.append(current)
    if lines[current[1]][current[0]] == "S":
        break

top = False

def check_top(x, y):
    """ Checks if the given coordinates are on the top of a chain item. """
    top = False
    for i in range(0,y):
        char = lines[i][x]
        if (x, i) in chain:
            if char in ["J", "7", "-"]:
                top = not top
    return top

count = 0
candidates = []
for y, line in enumerate(lines):
    left = False
    for x, char in enumerate(line):
        # Check to the left of the current character.
        if (x, y) in chain:
            # We crossed a chain item.
            if char in ["J", "L", "|"]:
                left = not left
        else:
            if left and check_top(x, y):
                candidates.append((x, y))
                count += 1
print(f"Count: {count}")

def display_board():
    """ Prints the board. Chain items are keep their original character. Candidates are marked with a star. All other characters are replaced with a space. """
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (x, y) in chain:
                print(lines[y][x], end="")
            elif (x, y) in candidates:
                print("*", end="")
            else:
                print(" ", end="")
        print()

display_board()