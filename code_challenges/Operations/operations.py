import operator

def arithmetic_operation(n: str) -> int:
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '//': operator.truediv
    }

    first_number_string = ''
    second_number_string = ''
    operator_string = ''

    operator_converted = ops.get(operator_string)
    print(type(operator_converted))

    # mathva = first_number_string operator_converted second_number_string




arithmetic_operation("12 + 12")  # ➞ 24 // 12 + 12 = 24
# arithmetic_operation("12 - 12")  # ➞ 24 // 12 - 12 = 0
# arithmetic_operation("12 * 12")  # ➞ 144 // 12 * 12 = 144
# arithmetic_operation("12 // 0")  # ➞ -1 // 12 / 0 = -1
