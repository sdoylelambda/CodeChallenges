Highest Index (With a Twist)

Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string.

Do not use max() or reassign it a value to the alphabet list.

sorted() is not best practice.

## UPER

Understand
Input: list = alphebet
Ex: "Flavio"

Output: string = "letter closest to end of alphebet" + that letter
Ex: "22v"

## Plan

Option 1
for letter in string:
if letter position < loop thru ouput arr
replace var/var
return var + var

## Option 2

for letter in alphabet:
add position to new dict (key=numberPosition, value=letter)
if letter position < loop thru ouput arr
replace dict
return dict as string

Option 3
for letter, index in string:

Execute

Revise
