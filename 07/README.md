# Thoughts

- The challenge is getting the rank of each hand.
- There conveniant implementations for getting the rank using scipy and numpy (no need to re-invent the wheel)
- I could assign a score to each hand.

## Approach 1

- for each hand
  - get the rank of the hand (five of a kind: 7, four of a kind: 6, ...)
  - Get the rank of the first card (A:13, K:12, Q:11, J:10, T:9, 9:8, ...) 
    - it might would be easier to do this in base 13.
  - Get the rank of each following card...
  - Derive the score.
  - Append to score array
  - Append bid to second array
- Get the rank using scipy
- multiply rank vector with bid vector
