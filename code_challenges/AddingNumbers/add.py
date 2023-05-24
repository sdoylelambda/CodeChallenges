# def add(n1, n2):
#     if n1 == "" or n1 is None or n2 == "" or n2 is None:
#         return 'Invalid Operation'
#
#     int_value = int(n1) + int(n2)
#     return str(int_value)

def add(n1, n2):
    if n1 == "" or n2 == "":
        print('Invalid Operation')
        return 'Invalid Operation'

    int_value = int(n1) + int(n2)
    print(str(int_value))
    return str(int_value)


# add("111", "111")  # ➞ "222"
# add("10", "80")  # ➞ "90"
add(None, "20")  # ➞ "Invalid Operation"
