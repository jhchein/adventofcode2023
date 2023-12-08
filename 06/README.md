# Day 06 of Advent of Code 2023

## Challenge Overview

(*Created with [Tech Writer Pro](https://chat.openai.com/g/g-Qu7c6GDqP-tech-writer-pro) GPT*)

**Day 06 of Advent of Code 2023** presents a unique challenge involving a toy boat race. The essence of the challenge lies in optimizing the boat's movement within a given time frame to surpass a record distance. The boat's movement is governed by a simple yet intriguing mechanism: the longer you press the button at the start, the faster the boat moves, but this also eats into your total race time.

## Key Points in Understanding the Challenge

1. **Race Mechanics**: The boat starts with a speed of zero and gains speed linearly for each millisecond the button is held down. However, holding the button reduces the available time for the boat to move.
2. **Objective**: To find the optimal button hold time that allows the boat to travel farther than the current record for each race.
3. **Calculating Distance**: The distance traveled is the product of speed and remaining time after the button is released.

## My Thought Process

1. **Analyzing the Problem**: At first glance, the problem resembles finding the maximum area of a rectangle under a fixed perimeter constraint, where the perimeter is the total time and the area is the distance traveled.
2. **Optimization Strategy**: The optimal solution seems to be when the time spent accelerating and moving is balanced, akin to a square's sides being equal for maximum area.
3. **Mathematical Modeling**: The challenge can be mathematically modeled as a quadratic function, where we seek the range of times that yield a distance greater than the record.

## Implementation Strategies

Approach 1: Binary Search

- I first used a **binary search algorithm** to find the minimum speed that allows beating the record. This approach efficiently narrows down the speed range by halving the search space iteratively.

```python
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

Approach 2: Quadratic Formula

- For a faster and more mathematically elegant solution, I utilized the **quadratic formula**. This approach directly calculates the extreme points where the distance equals the record, thereby determining the range of viable speeds.

```python
# Derived from the equation record_distance = speed * (time-speed)
t_moving_max = floor(-p/2 + sqrt((p/2)**2 - q))
t_moving_min = ceil(-p/2 - sqrt((p/2)**2 - q))
```

## Conclusion

By approaching the problem with a combination of binary search and the application of quadratic equations, I was able to efficiently compute the solution, demonstrating both algorithmic thinking and mathematical prowess. This approach not only provided an optimal solution but also showcased the elegance of applying mathematical concepts to programming challenges.
