# Sum of Evenly Divisible Numbers from a Range
# returns the sum of the numbers that are
# evenly divided by c from the range a, b inclusive.


# Understand -
# Find range from a to b
# Find all nums that are divisible by c
# ann add them together
# return total

# Plan -

# Execute

# Revise


def evenly_divisible(a, b, c):
    nums_divisible_by_c = []
    for range_num in range(a, b + 1):
        if range_num % c == 0:
            nums_divisible_by_c.append(range_num)

    total = sum(nums_divisible_by_c)
    return total


evenly_divisible(1, 10, 20)  # ➞ 0
# # No number between 1 and 10 can be evenly divided by 20.
#
evenly_divisible(1, 10, 2)  # ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3)  # ➞ 18
# 3 + 6 + 9 = 18

