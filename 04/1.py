import re

def process_card(line):
    card_id = re.findall(r"Card\s+(\d+):", line)[0]
    winning_numbers, my_numbers = line.split(":")[1].split("|")
    winning_numbers = [int(n) for n in winning_numbers.split()]
    my_numbers = [int(n) for n in my_numbers.split()]
    matches = len(set(my_numbers) & set(winning_numbers))
    score = 2**(matches - 1) if matches > 0 else 0
    return score

with open("input.txt") as f:
    cards = f.read().splitlines()

total_score = sum(process_card(card) for card in cards)

print(f"Total score: {total_score}")