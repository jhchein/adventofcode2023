# Thoughts

## Facts

The problem can be seen as calculating the area of a square:

- total_time = moving_time + acceleration_time = moving_time + speed
- distance = speed * moving_time (<- Square)
- The largest distances are achieved if the sides of the square are of the same length (or almost, if time is odd).
- The problem is symmetric, therefore you can save half of the calculations.
- You aim for all distances larger than the record. -> We need to find the shortest acceleration_time (speed) for which the distance is still larger than the record distance.
- When then have the range of speed_min to speed_max, twice (as the problem is symmetric), plus 1 if time is an odd number.

## Approach

- To find min_speed, we do a binary search to find the smallest value between 1 and max_speed.

```Python
def find_min(a, b):
    low = 1
    high = a
    while low < high:
        mid = (low + high) // 2
        if mid * (a - mid) > b:
            high = mid
        else:
            low = mid + 1
    return low
```
