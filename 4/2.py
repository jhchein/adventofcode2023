import re

with open("input.txt") as f:
    cards = f.read().splitlines()

def process_card(line):
    card_id = int(re.findall(r"Card\s+(\d+):", line)[0])
    winning_numbers, my_numbers = line.split(":")[1].split("|")
    winning_numbers = [int(n) for n in winning_numbers.split()]
    my_numbers = [int(n) for n in my_numbers.split()]
    matches = len(set(my_numbers) & set(winning_numbers))
    
    new_cards = [card_id + i + 1 for i in range(matches)]
    return card_id, matches, new_cards

pile = {card_id + 1: 1 for card_id in range(len(cards))}

for card in cards:
    card_id, matches, new_cards = process_card(card)
    number_in_pile = pile[card_id]
    pile.update({card_id: pile[card_id] + number_in_pile for card_id in new_cards})

total_cards = sum(pile.values())
print(total_cards)