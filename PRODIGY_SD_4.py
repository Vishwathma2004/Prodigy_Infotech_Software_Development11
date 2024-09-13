def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_safe(grid, row, col, num):
    # Check if 'num' is not in the current row
    if num in grid[row]:
        return False

    # Check if 'num' is not in the current column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if 'num' is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(grid, row=0, col=0):
    # If we have reached the end of the grid, the puzzle is solved
    if row == 9:
        return True

    # Move to the next row if we have reached the end of the current row
    if col == 9:
        return solve_sudoku(grid, row + 1, 0)

    # Skip the cells that are already filled
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col + 1)

    # Try placing numbers 1 to 9 in the current cell
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0  # Backtrack

    return False  # Trigger backtracking

if __name__ == "__main__":
    grid = []
    print("Enter the Sudoku puzzle (use 0 for empty cells):")
    for _ in range(9):
        grid.append(list(map(int, input().split())))

    if solve_sudoku(grid):
        print("Solved Sudoku puzzle:")
        print_grid(grid)
    else:
        print("No solution exists.")
