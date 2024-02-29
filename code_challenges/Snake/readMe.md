The Snake — Area Filling
This challenge is based on the classic videogame "Snake".

Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.

length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).

Create a function that takes the side n of the game screen and returns the number of times the snake can eat before it runs out of space in the game screen.


UPER

Understand
Input: number of tiles on each axis
Output: Max number can eat

Can move on all blocks: n * n = total moves
Double each time it eats
If double makes snake longer than total number of blocks, 
return number of times it has eaten


Plan
Find total size of board (snake can be half)
Keep track of each time snake eats
Keep track of length of snake
If eating again 
Causes snakeSize > boardSize
return count
else
count += 1
snake *= 2

Execute

Revise

