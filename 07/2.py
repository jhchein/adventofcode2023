import re
from scipy.stats import rankdata
from collections import Counter

hands_and_bids_pattern = re.compile(r"([23456789TJQKA]+)\s(\d+)")

card_value_map = {
    **{str(i): i for i in range(2, 10)},
    **{"T": 10, "J": 1, "Q": 11, "K": 12, "A": 13}
}

rank_mapping = {
        (5, ): 7,  # Five of a kind
        (4, 1): 6,  # Four of a kind
        (3, 2): 5,  # Full house
        (3, 1, 1): 4,  # Three of a kind
        (2, 2, 1): 3,  # Two pair
        (2, 1, 1, 1): 2,  # One pair
        (1, 1, 1, 1, 1): 1  # High card
    }

def convert_array_to_base13(arr: list) -> int:
    return sum(val * (13 ** (len(arr) - i - 1)) for i, val in enumerate(arr))

def calculate_hand_rank(hand: str) -> int:
    if len(set(hand)) == 1:
        return 7  # Five of a kind
    cards_except_jokers = [card for card in hand if card != "J"]
    number_of_jokers = 5-len(cards_except_jokers)
    hand_counts = sorted(Counter(cards_except_jokers).values(), reverse=True)
    hand_counts[0] += number_of_jokers
    return rank_mapping[tuple(hand_counts)]

def calculate_hand_score(hand: str) -> int:
    score = [calculate_hand_rank(hand), *[card_value_map[card] for card in hand]]
    result = convert_array_to_base13(score)
    return result

### PARSE THE INPUT ###
with open("input.txt", "r") as f:
    lines = f.readlines()

# ### SOLVE THE PROBLEM ###
hand_list, bid_list = zip(*[hands_and_bids_pattern.findall(line)[0] for line in lines])
score_list = [calculate_hand_score(hand) for hand in hand_list]
bid_list = [int(bid) for bid in bid_list]

rank_list = rankdata(score_list)

print(int(sum(rank_list * bid_list)))
