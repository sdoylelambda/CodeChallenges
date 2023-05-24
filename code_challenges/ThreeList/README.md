Three Lists!
Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.

UPER

U - UNDERSTAND
INPUT - 3 lists of numbers
OUTPUT - Number 

Find matching numbers in all lists
Add them all together
May be more or less than one match in each list

P - PLAN
3 nested loops
if in all 3
+= output


E - EXECUTE


R - REVISE



def sum_common(lst1, lst2, lst3):
    pass


Examples
sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]) ➞ 5
// 2 & 3 are common in all 3 lists.

sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]) ➞ 7
// 2, 2 & 3 are common in all 3 lists.

sum_common([1], [1], [2]) ➞ 0
