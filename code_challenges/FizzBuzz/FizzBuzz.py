# UPER

# Understand
# Take in num
# Return string always (even if num)


# Plan
# [x] If the number is a multiple of 3 the output should be "Fizz".
# [x] If the number given is a multiple of 5, the output should be "Buzz".
# [x] If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# [x] If the number is not a multiple of either 3 or 5, return the number as a string

# Revise
# if statements - factory pattern, switch/case

# working
def fizz_buzz(num: int) -> str:
    # Execute
    if num % 5 == 0 and num % 3 == 0:
        print("FizzBuzz")
        return "FizzBuzz"
    if num % 3 == 0:
        print("Fizz")
        return "Fizz"
    if num % 5 == 0:
        print("Buzz")
        return "Buzz"
    else:
        print(str(num))
        return str(num)


# def fizz_buzz(num):
#     return "Fizz"*(num % 3 == 0) + "Buzz"*(num % 5 == 0) or str(num)

#
# def fizz_buzz(num):
#     s = ''
#     if num % 3 == 0: s += 'Fizz'
#     print(s)
#     if num % 5 == 0: s += 'Buzz'
#     print(s)
#     return s if s else str(num)


fizz_buzz(3)  # ➞ "Fizz"

fizz_buzz(5)  # ➞ "Buzz"

fizz_buzz(15)  # ➞ "FizzBuzz"

fizz_buzz(4)  # ➞ "4"




















