# def stair(steps: int) -> str:
#     x = "  _\n_|"
#
#     if steps == 0:
#         return '---'
#     if steps == 1:
#         return "  _\n_|"
#
#     space = ' '
#     output = ''
#
#     while steps > 0:
#
#         while steps > 0:
#             space += ' '
#
#         output += space
#         output += x
#         steps -= 1
#         print(output)
#
#     print(output)
#     return output


def stair(steps: int) -> str:
    spaces = steps * 2
    output_string = ''

    if steps == 0:
        return '___'

    # start spaces = steps * 2 (then subtract 2 each iteration)     join()
    # for each spaces output_string += ' '
    count = spaces
    while count > 0:
        output_string += ' '
        count -= 1
        print("while", output_string)

    # for the top step, add "_\n"
    output_string += '_\n|'
    print("no loop", output_string)
    # For each stair
    while steps > 2:
        loop_count = spaces - 2
        print('count', count)
        while loop_count > 0:
            output_string += " "
            loop_count -= 1
            # for the middle steps, add "_|\n"
        output_string += '_|\n'
        print("while2", output_string)

        steps -= 1

    # for the last step, add "_|\n_|"    prob need spaces here
    output_string = '  '
    output_string += '_|\n'
    print('OUTPUT')
    print(output_string)
    print("    _\n  _|\n_|")
    return output_string


# Examples
# stair(1)  # ➞ "  _\n_|"
# # 2 spaces, 1 underscore, 1 newline, 1 underscore, 1 vertical line
#
stair(2)  # ➞ "    _\n  _|\n_|"
# # 4 spaces, 1 underscore, 1 newline, 2 spaces, 1 underscore,
# # 1 vertical line, 1 newline, 1 underscore, 1 vertical line
#
# stair(3) ➞ "      _\n    _|\n  _|\n_|"
# # 6 spaces, 1 underscore, 1 newline, 4 spaces, 1 underscore,
# # 1 vertical line, 1 newline, 2 spaces, ...
#
# stair(4) ➞ "        _\n      _|\n    _|\n  _|\n_|"
# 8 spaces, 1 underscore, 1 newline, 6 spaces, 1 underscore,
# 1 vertical line,  ...















