Up the Hill, Down the Hill

Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate. Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.

Ex:

Person traveled up a hill for 18mins at 20mph and then
traveled back down the same path at 60mph
then their average speed traveled was 30mph.

Note:
The solution is not dividing the sum of the speeds by 2.

Questions:
DownHillTime - do we need to figure out? - down_spd / up_spd

UPER

U - Understand
Input: UpHillTime, UpHillSpeed, DownHillSpeed
Return: Average speed - int

Solve for DownHillTime
Solve for miles traveled up hill speed
solve for miles traveled down hill speed
return avg

Ex:
UpHillTime = 18 (min)
UpHillSpeed = 20 (mph)
DownHillSpeed = 60 (mph)
DownHillTime = 6 (min)

Helper Method
going 60 1/3 of the time
going 20 2/3 of the time
answer = 30

Math:
60/20 = 3
18/3 = 6

20.3

Ex: DownHillTime
speed_dif = DownHillSpeed / UpHillSpeed
DownHillTime = UpHillSpeed / divde_UpHillTime

went 20 miles for 15 min
15/4
