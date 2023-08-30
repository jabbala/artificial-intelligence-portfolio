def is_valid(puzzle: list, row: int, col: int, num: int) -> bool:
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
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if puzzle[start_row + i][start_col + j] == num:
                    return False
        return True


def solve(puzzle) -> bool:
    """The solve function defined to take the 2D and 9*9 sudoku to solve and 
    fill all zeros with appropriate numbers.

    Args:
        puzzle (list): puzzle

    Returns:
        bool: solved or no solution
    """
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if solve(puzzle):
                            return True
                        puzzle[row][col] = 0
                return False
    return True


def print_board(puzzle) -> None:
    """Display puzzle board

    Args:
        puzzle (list): Puzzle board
    """
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
        if i == 2 or i == 5:
            print("-" * 21)


if __name__ == "__main__":
    puzzle = [
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
    
    if solve(puzzle):
        print("Sudoku puzzle solved:")
        print_board(puzzle)
    else:
        print("No solution exists for the puzzle.")
