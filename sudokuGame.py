def solve_sudoku(board):
    """
    Solves a Sudoku board using backtracking algorithm.
    :param board: List[List[int]] - 9x9 grid representing the Sudoku board
    :return: bool - True if the board is solvable, False otherwise
    """
    # Find the next empty cell on the board
    row, col = find_empty_cell(board)

    # If there is no empty cell, the board is already solved
    if row is None:
        return True

    # Try all possible values for the empty cell
    for val in range(1, 10):
        if is_valid(board, row, col, val):
            # If the value is valid, update the board and continue with the next empty cell
            board[row][col] = val
            if solve_sudoku(board):
                return True
            # If the board cannot be solved with the current value, backtrack and try the next one
            board[row][col] = None

    # If no value can be placed in the current empty cell, the board is unsolvable
    return False


def find_empty_cell(board):
    """
    Finds the next empty cell on the board.
    :param board: List[List[int]] - 9x9 grid representing the Sudoku board
    :return: Tuple[int, int] or None - (row, col) of the next empty cell, or None if there is no empty cell
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] is None:
                return row, col
    return None


def is_valid(board, row, col, val):
    """
    Checks if a value can be placed in a cell on the board without violating any Sudoku rules.
    :param board: List[List[int]] - 9x9 grid representing the Sudoku board
    :param row: int - row index of the cell to check
    :param col: int - column index of the cell to check
    :param val: int - value to be placed in the cell
    :return: bool - True if the value is valid, False otherwise
    """
    # Check row
    for i in range(9):
        if board[row][i] == val:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == val:
            return False

    # Check subgrid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(subgrid_row, subgrid_row+3):
        for j in range(subgrid_col, subgrid_col+3):
            if board[i][j] == val:
                return False

    # If the value does not violate any rules, it is valid
    return True
