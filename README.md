# sudoku 🔢

## Generating the solution
I generated the solution using recursion. I randomly generated the first three square across the diagonal, this way I only had to worry about following the rule of the square and not the rows and columns. After those were added I added each square at a time adding a random number that follows the rules of the game. If it ran out of possible numbers to add, the program would restart that square by recursively calling the same function. If the program was unable to add that square it would backtrack to the previous square and so on. If it got back to the first square through recursion (not including the first initial 3 squares) it would restart the entire board.

## Generating solving algorithm
In progress, I have this algorithm working with one test case.

## Generating the board
Not complete

## Generating game play
Not complete


