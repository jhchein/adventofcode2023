# Camel Cards - Advent of Code 2023, Day 7

(*Created with [Tech Writer Pro](https://chat.openai.com/g/g-Qu7c6GDqP-tech-writer-pro) GPT*)

## Overview

This Python project addresses the Day 7 challenge of Advent of Code 2023, titled "Camel Cards." The challenge involves ranking poker-like hands and calculating their scores. The code leverages `scipy` and `numpy` for efficient computation.

## Challenge Summary

- Each hand in Camel Cards is ranked based on its type and the individual card ranks.
- Types range from 'Five of a kind' (strongest) to 'High card' (weakest).
- Hands are sorted based on type, then individual card strength in descending order.
- In Part 2 Jokers (J cards) act as wildcards but are the weakest when breaking ties.
- The final score is calculated by multiplying each hand's bid by its rank.

## Approach

1. **Rank Calculation**: Determine the rank of each hand based on predefined rules.
2. **Score Derivation**: Convert hand ranks and card values to a base 13 system for scoring.
3. **Final Computation**: Use `scipy.rankdata` to rank the hands, then calculate total winnings by multiplying ranks with bids.

> Note: The code includes two parts: 1.py for the basic version and 2.py for the extended version with the joker rule.

## Running the Code

- Ensure `scipy` and `numpy` are installed.
- Execute `1.py` or `2.py` depending on the challenge part.
