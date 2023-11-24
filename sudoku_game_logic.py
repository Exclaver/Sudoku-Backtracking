def valid_move(x, i, j, arr):
    """
    Check if placing a number 'x' at position (i, j) in a Sudoku grid is valid.

    Args:
    x (int): The number to be placed in the Sudoku grid.
    i (int): The row index where the number is to be placed.
    j (int): The column index where the number is to be placed.
    arr (list of lists): The Sudoku grid represented as a 2D list.

    Returns:
    bool: True if the move is valid, False otherwise.
    """
    if row(x, i, arr) and column(x, j, arr) and casket(x, i // 3, j // 3, arr):
        return True
    else:
        return False

def row(x, i, arr):
    """
    Check if a number 'x' can be placed in row 'i' of the Sudoku grid.

    Args:
    x (int): The number to be checked.
    i (int): The row index to be checked.
    arr (list of lists): The Sudoku grid.

    Returns:
    bool: True if the number can be placed, False if it already exists in the row.
    """
    for j in range(0, 9):
        if x == arr[i][j]:
            return False
    return True

def column(x, j, arr):
    """
    Check if a number 'x' can be placed in column 'j' of the Sudoku grid.

    Args:
    x (int): The number to be checked.
    j (int): The column index to be checked.
    arr (list of lists): The Sudoku grid.

    Returns:
    bool: True if the number can be placed, False if it already exists in the column.
    """
    for i in range(0, 9):
        if x == arr[i][j]:
            return False
    return True

def casket(x, i, j, arr):
    """
    Check if a number 'x' can be placed in a 3x3 box (casket) in the Sudoku grid.

    Args:
    x (int): The number to be checked.
    i (int): The row index of the 3x3 box.
    j (int): The column index of the 3x3 box.
    arr (list of lists): The Sudoku grid.

    Returns:
    bool: True if the number can be placed, False if it already exists in the box.
    """
    for k in range(0,3):
        for m in range(0,3):
            if x == arr[i*3 + k][j*3 + m]:
                return False
    return True