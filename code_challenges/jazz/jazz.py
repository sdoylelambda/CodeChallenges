# def jazzify(lst: list) -> list:
#     output_list = []
#     for chord in lst:
#         if not chord.endswith('7'):
#             chord.join('7')
#         output_list.append(chord)
#
#     print('output:', output_list)
#     return output_list
#
#
# def jazzify(lst: list) -> list:
#     return [chord if chord.endswith('7') else chord + '7' for chord in lst]
#
# def jazzify(lst: list) -> list:
#     return [chord if chord.endswith('7') else chord + '7' for chord in lst]
#
#
# jazzify(["G", "F", "C"])  # ➞ ["G7", "F7", "C7"]
# jazzify(["Dm", "G", "E", "A"])  # ➞ ["Dm7", "G7", "E7", "A7"]
# jazzify(["F7", "E7", "A7", "Ab7", "Gm7", "C7"])  # ➞ ["F7", "E7", "A7", "Ab7", "Gm7", "C7"]
#









# White method that takes in a list and if a word has a period at the end remove it
# Stretch goal unless D.C.

word_list = ['MD.', 'FL', 'ME.', 'CA.', 'AZ', 'D.C.']  # expect ['MD', 'FL', 'ME', 'CA', 'AZ']


# def remove_periods(word_list: list) -> list:
#     x = [state if not state.endswith('.') or state == 'D.C.' else state[:-1] for state in word_list]
#     print(x)
#     return x


# def remove_periods(word_list: list) -> list:
#     print(word_list)
#     for index in range(len(word_list)):
#         word = word_list[index]
#         if not word.endswith('.') or word == 'D.C.':
#             pass
#         else:
#             word_list[index] = word[:-1]















# def remove_periods(word_list):
#     for index in range(len(word_list)):
#         word = word_list[index]
#         if word.endswith('.') or word.upper() == 'D.C.':
#             word_list[index] = word[:-1]
#
#     print('output', word_list)
#     return word_list
#
#
# remove_periods(word_list)


# input_arr = ['Wo2rld', '!3', 'He1llo', '7Time', 'F5or', 'Next6', 'Go4od']
#
#
# def put_in_order(input_arr: list) -> list:
#     output_arr = [None] * len(input_arr)
#     for index in range(len(input_arr)):
#         str = input_arr[index]
#         for char in str:
#             if char.isnumeric():
#                 output_order = int(char)
#                 print(output_order)
#                 output_arr[output_order - 1] = str
#
#     print(output_arr)
#     return output_arr
#
#
# put_in_order(input_arr)


input_arr = ['Wo2rld', '!3', 'He1llo', '7Time', 'F5or', 'Next6', 'Go4od']


def put_in_order(input_arr: list) -> list:
    output_arr = [None] * len(input_arr)
    for index in range(len(input_arr)):
        word = input_arr[index]
        for letter in word:
            if letter.isnumeric():
                output_arr[int(letter) - 1] = word

    print(output_arr)
    return output_arr


put_in_order(input_arr)

