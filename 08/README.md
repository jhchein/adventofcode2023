# Thoughts

## Day 08 part 1

Part 1 is pretty straightforward:

- You parse the map as a nested dict with `node`, and the `L` and `R` keys.
- You parse the LR instructions as a list and infinely interate over them.
  - Once you encounter the "ZZZ" node, you break the loop.
  - You could use try except Stopiteration, but itertools cycle is more efficient and cleaner.

## Day 08 part 2

This part has a twist:

We start parallelizing the search for multiple starting nodes. Unfortunately it's quite unlikely to hit Z nodes for all six starting nodes.

The instructions lead us to cylce the map (otherwise it would stop in a dead-end). For example starting at node 1 we might encounter a Z node after [2,4,6] steps, while node 2 encounters a Z node after [3,5,6,9,10,12] steps. We can now calculate the `least common multiple` of the cycle times of each starting node to find the number of steps required to reach the end of the desert. Given that we can use the LCM, there is no more need to parallelize the search.
