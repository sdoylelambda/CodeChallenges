Instant JAZZ

Create a function which concatenates the number 7 to the end of every chord in a list. 

Ignore all chords which already end with 7.

Return an empty list if the given list is empty.

You can expect all the tests to have valid chords.

UPER

U - Understand
add 7 to each string in list
unless already has a 7
if empty return empty

P - Plan
Option 1
for each item in list
if does not end in 7
add 7
return new updated list

Option 2
Use Regex 
check last value
if not 7
add 7


E - Execute
Option 1
[] - for each item in list
[] - if does not end in 7
[] - add 7
[] - return new updated list

R - Revise
Option 2 - refactor
updated existing list instead of creating new output list