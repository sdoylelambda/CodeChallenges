arr = []


def flipping_bits(n):
    # Take input num and convert (to binary) to 32 bits.
    print(bin(n))
    y = bin(n)
    print(fromhex(y))
    # decimal_to_binary(n, arr)
    # Change all 0's to 1's and all 1's to 0's.
    # Option 1. - turn number into arr
    # for x in arr:
    #     if x is 0:
    #     x = 1
    # else:
    #     x = 0
    # Option2
    #     ternary
    #
    # Turn 32 bit into number
    # return number

#
# def decimal_to_binary(n, arr):
#     if n > 1:
#         # divide with integral result
#         # (discard remainder)
#         arr.append(n % 2)
#         decimal_to_binary(n // 2, arr)
#
#     print(n % 2, end=' ')
#
#
# print(arr)


# Examples
flipping_bits(4)  # ➞ 4294967291
# flipping_bits(2147483647)  # ➞ 2147483648
# flipping_bits(1)  # ➞ 4294967294

