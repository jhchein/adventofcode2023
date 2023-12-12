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

board = {
    (x, y): [(x+dx, y+dy) for dx, dy in connecting_nodes[char] if 0 <= x+dx < len(lines[0]) and 0 <= y+dy < len(lines)]
    for y, line in enumerate(lines)
    for x, char in enumerate(line.strip())
    if char != "."
}

start = next((coord for coord, neighbors in board.items() if "S" in lines[coord[1]][coord[0]]), None)
board[start] = [neighbor for neighbor in board[start] if start in board.get(neighbor, [])]

count = 0
prev, current = start, board[start][0]
while True:
    count += 1
    board[current].remove(prev)
    prev, current = current, board[current][0]
    if lines[current[1]][current[0]] == "S":
        break

print(f"Count: {ceil(count/2)}")