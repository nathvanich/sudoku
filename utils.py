# 1. utils.py ----------------------------
# 1.1 define rows:
rows = 'ABCDEFGHI'

# 1.2 define cols:
cols = '123456789'


# 1.3 cross(a,b) helper function to create boxes, row_units, column_units, square_units, unitlist
def cross(a, b):
    return [s + t for s in a for t in b]


# 1.4 create boxes
boxes = cross(rows, cols)

# 1.5 create row_units
row_units = [cross(r, cols) for r in rows]

# 1.6 create column_units
column_units = [cross(rows, c) for c in cols]

# 1.7 create square_units for 9x9 squares
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]

# 1.8 create unitlist for all units
unitlist = row_units + column_units + square_units

# 1.9 create peers of a unit from all units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


# 1.10 display function receiving "values" as a dictionary and display a 9x9 suduku board
def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    return
