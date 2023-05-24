# def sum_common(lst1, lst2, lst3):
#     output = 0
#     lst1.sort()
#     lst2.sort()
#     lst3.sort()
#     for number in lst1:
#         if number in lst2 and number in lst3:
#             output += number
#             # Remove first element from list in python
#
#             lst1.remove(lst1[0])
#             lst2.remove(lst2[0])
#             lst3.remove(lst3[0])
#             if len(lst1) == 0:
#                 break
#
#     print(output)
#     return output


# def sum_common(lst1, lst2, lst3):
#     output = 0
#     lst1.sort()
#     lst2.sort()
#     lst3.sort()
#
#     for number1 in lst1:
#         for number2 in lst2:
#             for number3 in lst3:
#                 if number1 is number2 and number2 is number3:
#                     output += number1
#         lst1.remove(lst1[0])
#         lst2.remove(lst2[0])
#         lst3.remove(lst3[0])
#         if len(lst1) == 0:
#             print(output)
#             return output

def sum_common(lst1, lst2, lst3):
    output = 0
    lst1.sort()
    lst2.sort()
    lst3.sort()
    count = len(lst1)
    while count > 0:
        if lst1[0] == lst2[0] and lst1[0] == lst3[0]:
            output += lst1[0]

        if lst1[0] < lst2[0] and lst1[0] < lst3[0]:
            lst1.remove(lst1[0])

        elif lst2[0] < lst1[0] and lst2[0] < lst3[0]:
            lst1.remove(lst1[0])

        elif lst3[0] < lst2[0] and lst3[0] < lst1[0]:
            lst1.remove(lst1[0])

        else:
            lst1.remove(lst1[0])
            lst2.remove(lst2[0])
            lst3.remove(lst3[0])
        count -= 1

    print(output)
    return output

    # if same value add to output value


# Examples
# sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2])  # ➞ 5
# # // 2 & 3 are common in all 3 lists.
#
# sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2])  # ➞ 7
# # // 2, 2 & 3 are common in all 3 lists.
#
# sum_common([1], [1], [2])  # ➞ 0

sum_common([1, 2, 2, 3, 2], [5, 3, 2, 2, 1], [7, 3, 2, 2, 1])  # 8
