"""Solve Sudoku Problem"""
PUZZLE_OUTER: list = [
    [0, 9, 8, 6, 4, 1, 0, 3, 7],
    [0, 0, 7, 8, 0, 0, 9, 4, 6],
    [0, 3, 6, 0, 0, 9, 8, 2, 0],
    [8, 5, 9, 2, 3, 6, 1, 7, 0],
    [0, 0, 0, 0, 9, 8, 3, 5, 2],
    [3, 0, 0, 1, 0, 7, 6, 9, 8],
    [0, 6, 0, 0, 1, 0, 4, 0, 5],
    [9, 0, 5, 7, 6, 4, 0, 1, 0],
    [0, 0, 4, 3, 8, 5, 0, 0, 9],
]
def is_valid(row: int, col: int, num: int) -> bool:
    """Function checks for the valid entry

    Args:
        puzzle (list): puzzle 2Dboard
        row (int): row index number
        col (int): column index number
        num (int): valid number to check wether to update or not

    Returns:
        bool: if it is valid number return True, else False
    """
    for i in range(9):
        if PUZZLE_OUTER[row][i] == num or PUZZLE_OUTER[i][col] == num:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if PUZZLE_OUTER[start_row + i][start_col + j] == num:
                    return False
    return True


def solve() -> bool:
    """To solve and fill all zeros with appropriate numbers.

    Args:
        puzzle (_type_): puzzle

    Returns:
        bool: bolean
    """
    for row in range(9):
        for col in range(9):
            if PUZZLE_OUTER[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(row, col, num):
                        PUZZLE_OUTER[row][col] = num
                        if solve():
                            return True
                        PUZZLE_OUTER[row][col] = 0
                return False
    return True


def print_board() -> None:
    """Display puzzle board

    Args:
        puzzle (list): Puzzle board
    """
    print("-" * 25)
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            print(PUZZLE_OUTER[i][j], end=" ")
            if j == 2 or j == 5 or j == 8:
                print("|", end=" ")
        print()
        if i == 2 or i == 5:
            print("-" * 25)
    print("-" * 25)


if __name__ == "__main__":

    if solve():
        print("Sudoku puzzle solved:")
        print_board()
    else:
        print("No solution exists for the puzzle.")
