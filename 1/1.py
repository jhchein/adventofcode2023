import re

digit_regex = re.compile(r"\d")

def find_first_last_digit(s):
    first_digit = digit_regex.search(s).group()
    last_digit = digit_regex.search(s[::-1]).group()

    return int(
        f"{first_digit}{last_digit}"
    )

with open("input.txt", "r") as fh:
    data = fh.readlines()

sum_of_digits = sum(find_first_last_digit(line) for line in data)

print(sum_of_digits)
