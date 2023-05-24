# def atbash(txt):
#     output_str = ''
#     for letter in txt:
#         if letter.isnumeric():
#             output_str += letter
#         print(ord(letter))
#         asc = ord(letter)
#
#     print('output', output_str)
#
#
# atbash("1apple")  # ➞ "1zkkov"
#
def atbash(txt):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    reverse = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
    output_str = ''
    for letter in txt:
        if letter in alph:
            output_str += reverse[alph.index(letter)]
        else:
            output_str += letter
    print(output_str)
    return output_str


# def atbash(txt):
#     a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#     z = 'ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba'
#     s = ''
#     for i in txt:
#         if i in a:
#             s += z[a.index(i)]
#         else:
#             s += i
#     print(s)
#     return s
#






# if not isinstance(letter, str):
#     print('x')
#     output_str.join(letter)
# print(chr(letter))


atbash("Hello world!")  # ➞ "Svool dliow!"

atbash("Christmas is the 25th of December")  # ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
