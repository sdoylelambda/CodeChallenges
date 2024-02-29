# UPER

# Understand
# 2 functions

# int_to_str
# take in str
# return num

# str_to_int
# take in str
# return num

# Plan
# int_to_str
#

# Execute

# Revise


# Options
# regex maybe?
# high - get hex value
# low - '' + 'num'


# def int_to_str(num: int) -> str:
#     x = f"'{num}'"
#     print(x)
#     return x

# def int_to_str(num):
#     num[1, " ":]
#     print(num)
#     return num


def int_to_str(num: int) -> str:
    s = ''
    s += "\""
    s += f'{num}'
    s += '\"'
    print(s)
    return s


# Remove quotation marks
def str_to_int(num: str) -> int:
    num[1:-1]
    print(num)
    return num


int_to_str(4)  # ➞ "4"
int_to_str(29348)  # ➞ "29348"
str_to_int("4")  # ➞ 4
