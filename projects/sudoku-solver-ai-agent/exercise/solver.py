def solve(puzzle:list(list(int))) -> bool:
    """_summary_

    Args:
        puzzle (list): _description_

    Returns:
        bool: _description_
    """
    return False


if __name__=="__main__":
    puzzle = [
        [0, 9, 8, 6, 4, 1, 0, 3, 7],
        [0, 0, 7, 8, 0, 0, 9, 4, 6],
        [0, 3, 6, 0, 0, 9, 8, 2, 0],
        [8, 5, 9, 2, 3, 6, 1, 7, 0],
        [0, 0, 0, 0, 9, 8, 3, 5, 2],
        [3, 0, 0, 1, 0, 7, 6, 9, 8],
        [0, 6, 0, 0, 1, 0, 4, 0, 5],
        [9, 0, 5, 7, 6, 4, 0, 1, 0],
        [0, 0, 4, 3, 8, 5, 0, 0, 9]
    ]
    
    if solve(puzzle):
        print("Sudoku puzzle solved:")
    else:
        print("No solution exists for the puzzle.")