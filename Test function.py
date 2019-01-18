# 3. Test function.py ----------------------------
import function
import utils

grid_easy = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
grid_hard = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = function.grid_values(grid_easy)
print("The original Sudoku board is **********************************************")
utils.display(values)

new_values = function.reduce_puzzle(values)
print("\n")
print("After applying constrint propagaton (both eliminate and only_choice strategies)*****************")
utils.display(new_values)
