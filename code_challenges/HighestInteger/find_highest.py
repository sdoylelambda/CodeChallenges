# nums_in_order = [0]
#
#
# def find_highest(lst: list) -> int:
#     try:
#         x = lst.pop()
#         if x > nums_in_order[0]:
#             nums_in_order.insert(0, x)
#         find_highest(lst)
#     except Exception as e:
#         print(f'Answer: {nums_in_order[0]}')
#         return nums_in_order[0]


def find_highest(lst: list) -> int:
    count = len(lst)
    print(count)
    while count > 0:
        print('while count', count)
        if lst[0] < lst[1]:
            lst.remove(lst[0])
            print('if lst', lst)
        count = count - 1
        print('output count', count)
        find_highest(lst)
    print(lst[0])
    return lst[0]



# find_highest([-1, 3, 5, 6, 99, 12, 2])  # ➞ 99

find_highest([0, 12, 4, 87])  # ➞ 87

# find_highest([8])  # ➞ 8
