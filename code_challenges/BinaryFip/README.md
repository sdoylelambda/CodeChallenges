Flipping Bits
You will be given a list of 32-bit unsigned integers. Flip all the bits 1 -> 0 and 0 -> 1 and return the result as an unsigned integer.

Worked Example
n = 4
4 is 0100 in binary. We are working in 32 bits so:
00000000000000000000000000000100 = 4
11111111111111111111111111111011 = 4294967291
return 4294967291

Examples
flipping_bits(4) ➞ 4294967291

flipping_bits(2147483647) ➞ 2147483648

flipping_bits(1) ➞ 4294967294


UPER

U - UNDERSTAND
input: number
output: number

P - Plan
    Take input num and convert (to binary) to 32 bits.
    Change all 0's to 1's and all 1's to 0's.
    Turn 32 bit into number
    return number

E - Execute
Take input num and convert (to binary) to 32 bits.
Change all 0's to 1's and all 1's to 0's. 
Option 1. - turn number into arr
for x in arr:
    if x is 0:
    x = 1
else:
    x = 0
Option2
    ternary
 
Turn 32 bit into number
return number
    

Notes
    print(format(n, '08b'))
    print(bin(n))
