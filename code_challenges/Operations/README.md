Basic Arithmetic Operations on a String Number

Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number

(ex "12 + 24" or "23 - 21" or "12 // 12" or "12 \* 21").

eval() is not allowed.

Questions
How to use converted operator

-

UPER

## Understand

Input: string - ("12 + 12")
Output: int - 24

The operators are \* - + and //.
All the inputs are only integers.

Think about the single space that appears before and after the arithmetic operator.

In case of division, whenever the second number equals "0" return -1.
ex "15 // 0" returns -1

## Plan

Option 1
use regex to find
1st num
2nd num
operater

Option 2
loop thru string
if value is a number add to a new string - 1st num
2nd num

if value is "+"
return 1st + 2nd

if is - etc

## Execute

## Revise
