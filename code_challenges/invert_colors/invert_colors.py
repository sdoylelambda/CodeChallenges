def color_invert(rgb: tuple) -> tuple:
    nums = list(range(0, 256))
    reversed_nums = nums
    reversed_nums.reverse()
    inverted_rgb_arr = []

    for num_color in rgb:
        # Find index value 2nd list
        index_value = nums[num_color]
        print('index_value', index_value)
        inverted_rgb_arr.append(index_value)

    print(tuple(inverted_rgb_arr))
    return tuple(inverted_rgb_arr)

color_invert((165, 170, 119))  # ➞ (0, 0, 0)

