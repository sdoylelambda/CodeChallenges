# UPER

# UNDERSTAND
# return non prime positive numbers
#

# Plan
# How to find prime numbers?
# Options
# Loop thru all numbers half or smaller
# Use range by value of 2
# if n divided by above is 0 (is prime pass)
# return non prime

# Handle negative values
# if less than 0 pass


print(type(2/3))


def manipulate_generator(g, n):
    # Enter your code here
    count = 0
    if n == 1:
        count += 1
        print('count1,', count)
        print('return: 1')

        return 1
    elif n > 1:
        # Loop thru all numbers half or smaller
        # n = n + 3
        print('NNNNN', n)
        while count < n:
            num = range(2, 24)
            # Use range by value of 2
            # if n divided by above is 0 (is prime pass)
            if n % num == 0:
                # return non prime
                print('return:', n)
                count += 1
                print('count::2::', count)
                return num

        print('count::::', count)

        if count > n:
            print('break', count)


# def manipulate_generator(g,n):
#     if n == 1:
#         print(n)
#         return 1
#     if n > 1:
#     # Loop thru all numbers half or smaller
#         for num in range(2, n):
#             # Use range by value of 2
#             # if n divided by above is 0 (is prime pass)
#             if n % num == 0:
#                 # return non prime
#                 print(num)
#                 return num

# def manipulate_generator(g, n, count):
#     # Enter your code here
#     print('count', count)
#     while count < n:
#         if n == 1:
#             print('return: 1')
#             count += 1
#             return 1
#         if n > 1:
#             # Loop thru all numbers half or smaller
#
#             for num in range(2, n):
#                 print(num)
#                 # Use range by value of 2
#                 # if n divided by above is 0 (is prime pass)
#                 if n % num == 0:
#                     # return non prime
#                     print('return:', n)
#                     count += 1
#                     return num
#
#         last_entry = range


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = int(12)
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    # print('n:::::', n)
    manipulate_generator(g, n)
