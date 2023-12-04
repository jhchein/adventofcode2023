import re

# Compiled regexes for finding the first and last digit in a string
digit_regex = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")
reversed_digit_regex = re.compile(r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin")

# replace all written numbers with digits
replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}

def find_first_last_digit(s):
    first_digit = digit_regex.search(s).group()
    last_digit = reversed_digit_regex.search(s[::-1]).group()

    return int(
        f"{replacements.get(first_digit, first_digit)}{replacements.get(last_digit[::-1], last_digit[::-1])}"
    )

with open("input.txt", "r") as fh:
    data = fh.readlines()

sum_of_digits = sum(find_first_last_digit(line) for line in data)

print(sum_of_digits)

