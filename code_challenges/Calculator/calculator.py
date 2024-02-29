import operator as built_in


def calculator(num1, operator, num2):
    if num2 == 0:
        return "Can't divide by 0!"
    built_in_operator = {"+": built_in.add, "-": built_in.sub, "*": built_in.mul, "/": built_in.truediv}
    print(built_in_operator[operator](num1, num2))
    solution = built_in_operator[operator](num1, num2)
    return solution


calculator(2, "+", 2)  # ➞ 4
calculator(2, "*", 2)  # ➞ 4
calculator(4, "/", 2)  # ➞ 2

# Working low level solution
# def calculator(num1, operator, num2):
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/' and num2 == 0:
#         return "Can't divide by 0!"
#     elif operator == '/':
#         return num1 / num2
