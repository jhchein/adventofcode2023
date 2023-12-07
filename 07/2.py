import re
from scipy.stats import rankdata

hands_and_bids = re.compile(r"([23456789TJQKA]+)\s(\d+)")

card_map = {
    **{str(i): i for i in range(2, 10)},
    **{"T": 10, "J": 1, "Q": 11, "K": 12, "A": 13}
}

def array_to_base13(arr):
    return sum(val * (13 ** i) for i, val in enumerate(arr[::-1]))

def hand_rank(hand: str) -> int:
    if len(set(hand)) == 1:
        return 7  # Five of a kind
    cards_except_jokers = [card for card in hand if card != "J"]
    number_of_jokers = 5-len(cards_except_jokers)
    hand_counts = sorted([hand.count(card) for card in set(cards_except_jokers)], reverse=True)
    hand_counts[0] += number_of_jokers

    rank_mapping = {
        (5, ): 7,  # Five of a kind
        (4, 1): 6,  # Four of a kind
        (3, 2): 5,  # Full house
        (3, 1, 1): 4,  # Three of a kind
        (2, 2, 1): 3,  # Two pair
        (2, 1, 1, 1): 2,  # One pair
        (1, 1, 1, 1, 1): 1  # High card
    }
    
    return rank_mapping[tuple(hand_counts)]

def score(hand: str) -> int:
    score = [hand_rank(hand), *[card_map[card] for card in hand]]
    result = array_to_base13(score)
    return result

### PARSE THE INPUT ###

with open("input.txt", "r") as f:
    lines = f.readlines()

# ### SOLVE THE PROBLEM ###

hands, bids = zip(*[hands_and_bids.findall(line)[0] for line in lines])
scores = [score(hand) for hand in hands]
bids = [int(bid) for bid in bids]

ranks = rankdata(scores)

print(int(sum(ranks * bids)))
