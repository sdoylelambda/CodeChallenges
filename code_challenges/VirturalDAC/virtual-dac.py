import math


def V_DAC(value):
    r = (value *(5.00 / 1023))
    print(round(r, 2))
    return round(r, 2)


V_DAC(0)  # ➞ 0
V_DAC(1023)  # ➞ 5
V_DAC(400)  # ➞ 1.96

# Test.assert_equals(V_DAC(1023), 5)
# Test.assert_equals(V_DAC(0), 0)
# Test.assert_equals(V_DAC(500), 2.44)
# Test.assert_equals(V_DAC(400), 1.96)
# Test.assert_equals(V_DAC(850), 4.15)
