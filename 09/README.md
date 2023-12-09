# Advent of Code - Day 9 Solutions

(*Created with [Tech Writer Pro](https://chat.openai.com/g/g-Qu7c6GDqP-tech-writer-pro) GPT*)

## Introduction

This README documents my solutions for Day 9 of the Advent of Code challenge. The challenge, titled "Mirage Maintenance," involves analyzing environmental data to predict the future state of an oasis. The data is a series of numbers where each line represents the history of a single value. The task is to predict the next value in each series.

## Solutions

### Part 1: Forward Extrapolation (1.py)

#### Overview part 1

The script `1.py` solves the first part of the challenge, which requires extrapolating the next value for each history in the input data.

#### Approach (part 1)

**Recursive Prediction**: A recursive function `predict_next_value` is implemented to calculate the next value in the series. This function works by:

- Computing the differences between adjacent values in the input series.
- Recursively calling itself with the newly computed series until a series with all zeroes is obtained.
- Once the series of zeroes is reached, the function calculates the next value in the original series.

#### Performance (part 1)

- The script demonstrates efficient computation by using recursion and list comprehensions.
- A notable aspect is the check for an all-zero sequence to terminate the recursion.

### Part 2: Backward Extrapolation (2.py)

#### Overview (part 2)

The script `2.py` addresses the second part of the challenge, where the task is to extrapolate backwards to predict the previous value in each history.

#### Approach (part 2)

**Adjusted Recursion**: Similar to `1.py`, but with a twist in the recursive function:

- The difference calculation is inverted to suit backward extrapolation.
- Instead of adding the last element of the original series, the first element is added in each recursive step.

#### Performance (part 2)

- The script maintains efficiency with a similar approach to `1.py`.
- The inverted difference calculation is a key change aligning with the challenge's requirements for backward extrapolation.

## Conclusion

These scripts demonstrate a clear and efficient approach to solving the given problem using Python's powerful features like regular expressions and recursion. The solutions are tailored to handle both forward and backward extrapolations, showcasing flexibility in algorithmic thinking.
