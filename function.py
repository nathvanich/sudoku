# 2. function.py ----------------------------
'''
Instruction: create grid_values(grid) A function to convert the string
representation of a puzzle into a dictionary form.
'''

# import utils


# 2.1 grid_values function (input> strong of sudoku problem, output> dictionary
# of a suduku with corresponding boxes)
import utils # remove this when use as a file


def grid_values(grid):
    # In this function, you will take a sudoku as a string
    # and return a dictionary where the keys are the boxes,
    # for example 'A1', and the values are the digit at each
    # box (as a string) or '.' if the box has no value
    # assigned yet

    value = utils.boxes
    dict_sudoku = {}

    for n in range(len(value)):
        if(grid[n] == '.'):
            dict_sudoku[value[n]] = '123456789'
        else:
            dict_sudoku[value[n]] = grid[n]

    return(dict_sudoku)


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    dictMain = values

    listKeys = list(dictMain.keys())
    # listKeys = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','B1']



    for i in listKeys:
        target_set = set()
        peer_set = set()
        elim_set = set()

        # Convert value in target boxes to set
        # for i in range(len(dict_sudoku['A1'])):
        #    target_set.add(dict_sudoku['A1'][i])
        target_set = set(dictMain[i])

        # Convert value in peer boxes to set
        for x in sorted(utils.peers[i]):
            peer_set.add(dictMain[x])
            # print(x + ":" + dict_sudoku[x])

        # Clean int value from peer set
        # peer_set.remove('123456789')
        # print('target_set:' + str(sorted(target_set)))
        # print('peer_set:' + str(sorted(peer_set)))

        # offset value in target boxes and all peer boxes
        elim_set = target_set.difference(peer_set)
        # print('elim_set:' + str(sorted(elim_set)))

        # convert elim_set back to str >>> ready to put back to dict
        # x = "".join(sorted(elim_set))
        # print(x)

        if bool(elim_set) is False:
            y = "".join(sorted(target_set))
            dictMain[i] = y
        else:
            x = "".join(sorted(elim_set))
            dictMain[i] = x

        # dictMain[i] = x

    return dictMain


def only_choice(values):

    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    dictMain = values

    listKeys = list(dictMain.keys())

    #print(utils.units['A1'])

    for key in listKeys:

        # create set of current values
        checkVal = set(dictMain[key])

        # list of neighbor boxes
        listBoxes = utils.units[key][2]

        # remove current key from neighbor set
        listBoxes.remove(key)

        #print(utils.square_units)
        if len(checkVal) != 1:

            setBoxes = set()

            # create set of neighbor values
            for i in listBoxes:
                tempSet = set(dictMain[i])
                setBoxes.update(tempSet)

            # find unique values
            x = checkVal.difference(setBoxes)

            # if
            if bool(x) is False:
                y = "".join(sorted(checkVal))
                dictMain[key] = y
            else:
                x = "".join(sorted(x))
                dictMain[key] = x


        else:
            y = "".join(sorted(checkVal))
            dictMain[key] = y

        listBoxes.insert(0, key)


    #print(utils.unitlist)
    #print(utils.units['A1'])

    return dictMain


def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """

    dictMain = values
    dictTemp = dict()
    x = 0
    y = 0

    '''
    while checkSolve(dictMain) != 81 and checkSolve(dictMain) != count:
        eliminate(dictMain)
        only_choice(dictMain)
        count = checkSolve(dictMain)
    '''

    while True:
        x = checkSolve(dictMain)
        if x == y:
            print("too hard!!!!")
            break
        elif x == 81:
            print("It's solved!!!!")
            break
        else:
            eliminate(dictMain)
            only_choice(dictMain)
            y = x


    return dictMain


def checkSolve(values):

    check = ''

    for x in values:
        check += values[x]

    '''
    if len(check) == 81:
        return check
    else:
        return check
    '''
    return len(check)



if __name__ == '__main__':

    grid_easy = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
    grid_hard = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'

    dict_sudoku = grid_values(grid_easy)

    reduce_puzzle(dict_sudoku)

    utils.display(dict_sudoku)
