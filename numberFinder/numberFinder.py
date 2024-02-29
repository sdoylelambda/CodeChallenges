# main points

# lets make a program to add 2 numbers together -- vocab words

# x = 5
# y = 1
#
#
# def add(x, y):
#     return print(x + y)
#
#
# def subtract(x, y):
#     return print(x - y)
#
# # make a method that multiplies numbers
# def multiply(x, y):
#     return print(x * y)
#
#
# # call/use function/program
# add(x, y)
# subtract(x, y)
# multiply(x, y)

# def - creates a new method/function/program
# print - makes it show up when running the program, - see solution
# return - solution that method/function/program finds

# dif colors -
# dark orange/purple - built in programs - stuff it already knows
# yellow - named by you -- what you are teaching you

# indention - 1 tab over


# def - used to create/define a new method/function/program

import random
import time
import sys
sys.setrecursionlimit(10000)


def number_finder(code, count=0):
    start_time = time.time()
    stored_attempts = []

    x = random.randrange(9)
    y = random.randrange(9)
    z = random.randrange(9)
    i = random.randrange(9)
    code_attempt = [x, y, z, i]

    if code != code_attempt and code_attempt not in stored_attempts:
        count += 1
        stored_attempts.append(code_attempt)
        number_finder(code, count)
        return code_attempt
    else:
        print('')
        print("Code found in", time.time() - start_time, " seconds to run.")
        print(f'Program ran {count} many times.')
        print(f'{code} is equal to {code_attempt}.')
        print('         Access granted')


# number_finder([8, 3, 6, 0], 0)























def hacker_pro(actual_password, number_of_attempts=0):
    start_time = time.time()
    failed_password_attempts = []
    password_attempt = four_random_numbers()

    if actual_password != password_attempt and password_attempt not in failed_password_attempts:
        number_of_attempts += 1
        failed_password_attempts.append(password_attempt)
        number_finder(actual_password, number_of_attempts)

    else:
        print('')
        print("Code found in", time.time() - start_time, " seconds to run.")
        print(f'Program ran {number_of_attempts} many times.')
        print('')
        print(f'{actual_password} is equal to {password_attempt}. Access granted')
        print('')


def four_random_numbers():
    x = random.randrange(9)
    y = random.randrange(9)
    z = random.randrange(9)
    i = random.randrange(9)
    code_attempt = [x, y, z, i]
    return code_attempt


# hacker_pro([8, 3, 6, 0], 0)


class MasterHacker:

    def hacker_pro(self, actual_password, number_of_attempts=0):
        start_time = time.time()
        failed_password_attempts = []
        password_attempt = self._four_random_numbers()

        if actual_password != password_attempt and password_attempt not in failed_password_attempts:
            number_of_attempts += 1
            failed_password_attempts.append(password_attempt)
            number_finder(actual_password, number_of_attempts)

        else:
            print('')
            print("Code found in", time.time() - start_time, " seconds to run.")
            print(f'Program ran {number_of_attempts} many times.')
            print('')
            print(f'{actual_password} is equal to {password_attempt}. Access granted')
            print('')

    def _four_random_numbers(self):
        x = random.randrange(9)
        y = random.randrange(9)
        z = random.randrange(9)
        i = random.randrange(9)
        code_attempt = [x, y, z, i]
        return code_attempt


Hacker = MasterHacker()
Hacker.hacker_pro([8, 3, 6, 0], 0)