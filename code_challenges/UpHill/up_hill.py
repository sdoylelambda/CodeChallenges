# def ave_spd(up_time: int, up_spd: int, down_spd: int) -> int:
#     speed_dif = down_spd / up_spd
#     down_time = up_time / speed_dif
#     print(down_time)
#     miles_up_hill = distance / 60

def ave_spd(up_time, up_spd, down_spd):
    distance = up_spd * (up_time / 60)
    down_time = distance / down_spd
    answer = 2 * distance / (up_time / 60 + down_time)
    print(answer)

ave_spd(18, 20, 60)  # ➞ 30
# ave_spd(30, 10, 30)  # ➞ 15
# ave_spd(30, 8, 24)  # ➞ 12
# Test.assert_equals(ave_spd(18, 10, 30), 15)
# Test.assert_equals(ave_spd(18, 20, 60), 30)
# Test.assert_equals(ave_spd(30, 10, 30), 15)
# Test.assert_equals(ave_spd(30, 8, 24), 12)


