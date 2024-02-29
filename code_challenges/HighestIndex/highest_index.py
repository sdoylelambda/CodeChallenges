def alphabet_index(alphabet: list, string: str) -> str:
    letter_dict = {}
    string_dict = string.split()
    for letter, position in map(string_dict, alphabet):
        # add position to new dict (key=numberPosition, value=letter)
        letter_dict.update({letter: position})
        print(letter_dict)

#   if letter position < loop thru ouput arr
#     replace dict
#   return dict as string




# Do not change
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

alphabet_index(alphabet, "Flavio")  # ➞ "22v"
alphabet_index(alphabet, "Andrey")  # ➞ "25y"
alphabet_index(alphabet, "Oscar")  # ➞ "19s"
