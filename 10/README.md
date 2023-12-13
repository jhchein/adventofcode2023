# Advent of Code Day 10

## Notes

- | is a vertical pipe connecting north and south.
- - is a horizontal pipe connecting east and west.
- L is a 90-degree bend connecting north and east.
- J is a 90-degree bend connecting north and west.
- 7 is a 90-degree bend connecting south and west.
- F is a 90-degree bend connecting south and east.
- . is ground; there is no pipe in this tile.
- S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

## Thoughts on Step 1

- We search for S.
- We start at S and check into each direction (NWSE) whether there is a connection.
- We recursively go into each viable direction (=parallel into multiple directions). -> No we'll max recursion depth
- We create an array ("chain") with all connecting pipes.
- Iterating through it, we need to remember, where we came from. Possibly by changing the node from a symbol to the current count.
- We stop once we return to S.
- Max distance is ceil(steps/2).

## Thoughts on Step 2

- This took a while ...!
- Tiles within the loop, have an odd amount of "closing" pipes to each direction. If there is an even amount, the loop is going around the tile.
- A closing pipe to the left is e.g. "|" or "L7" (closing from top to bottom).
- It's enough to check to e.g. the left and the top.
- We iterate over each tile and check to the left and top, if there is in both directions an odd amount closing pipes.
- It's probably easier and more performant to do this with matrix array, but given time constraints and low priority I postpone or skip that.
