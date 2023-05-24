Imaginary Coding Interview

Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

-

[x] - The candidate should have complete all the questions.

[x] - The maximum time given to complete the interview is 120 minutes.

[x] - The maximum time given for very easy questions is 5 minutes each.

[x] - The maximum time given for easy questions is 10 minutes each.

[x] - The maximum time given for medium questions is 15 minutes each.

[x] - The maximum time given for hard questions is 20 minutes each.

[x] - If all the above conditions are satisfied, return "qualified", else return "disqualified".

Given a list, in a true condition will always be in the format 
[very easy, very easy, easy, easy, medium, medium, hard, hard].

-

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

The maximum time to complete the interview includes a buffer time of 20 minutes.

Try to solve the problem using only list methods.

UPER

U - Understand - 10 min - till 2:30
Returns either "qualified" or "disqualified"
if tot value is greater than 120 return "disqualified"
check lst if any values do not meet criteria return "disqualified"
else return "qualified"
is data always valid? yes


P - Plan - 10 min  - till 2:40
options
if statement for reach requirment
if any fail then return "disqualified"
else return "qualified"

Itterate thru list and by position point check test result

Use boolean to return value

Or statmente(s)






























E - Execute - 10 min - till 2:50
R - Revise - 10 min - till 3

