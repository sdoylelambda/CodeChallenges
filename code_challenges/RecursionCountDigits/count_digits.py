count = 0


def digits_count(num: int) -> int:
    global count
    str_num = str(num)
    print('str_num', str_num)
    x = str_num[1:]
    print('x', x)
    print('len-x', len(x))
    while len(x) > 1:
        count += 1
        print('loop', x)
        print('loopint(x)', int(x))
        digits_count(int(x))

    print('count', count)
    return count


digits_count(123)  # ➞ 4
# digits_count(544)  # ➞ 3
# digits_count(121317)  # ➞ 6
# digits_count(0)  # ➞ 1
# digits_count(12345)  # ➞ 5
# digits_count(1289396387328)  # ➞ 13
# digits_count(3.2e6)  # ➞ 7
# digits_count(314890e3)  # ➞ 9
# digits_count(-1232323)  # ➞ 7


# x = 3
# i = str(x)
# slicer1 = i[1:]
# print(slicer1)
