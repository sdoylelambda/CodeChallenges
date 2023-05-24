def number_length(num):
    counter = 0
    for i in str(num):
        counter += 1

    print(counter)
    return counter


number_length(10)  # ➞ 2
number_length(5000)  # ➞ 4
number_length(0)  # ➞ 1

