def find_highest(lst):
    if len(lst) > 1:
        if lst[0] < lst[1]:
            lst.remove(lst[0])
        else:
            lst.remove(lst[1])
        find_highest(lst)

    else:
        print(lst[0])
        return lst[0]


# find_highest([-1, 3, 5, 6, 99, 12, 2])  # ➞ 99

find_highest([0, 12, 4, 87])  # ➞ 87

# find_highest([8])  # ➞ 8
