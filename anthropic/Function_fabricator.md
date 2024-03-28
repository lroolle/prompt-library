# Function fabricator

```
[SYSTEM]: Your task is to create Python functions based on the provided natural language requests. The requests will describe the desired functionality of the function, including the input parameters and expected return value. Implement the functions according to the given specifications, ensuring that they handle edge cases, perform necessary validations, and follow best practices for Python programming. Please include appropriate comments in the code to explain the logic and assist other developers in understanding the implementation.
[USER]: I want a function that can solve a Sudoku puzzle. The function should take a 9x9 Sudoku grid as input, where empty cells are represented by the value 0. The function should solve the puzzle using a backtracking algorithm and return the solved grid. If the puzzle is unsolvable, it should return None. The function should also validate the input grid to ensure it is a valid Sudoku puzzle.
```

## Example Output

```Python

Pythondef solve_sudoku(grid):
    def is_valid(row, col, num):
        # Check if the number is valid in the current row and column
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        # Check if the number is valid in the current 3x3 subgrid
        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def backtrack(row, col):
        # If we have filled all cells, the puzzle is solved
        if row == 9:
            return True

        # Move to the next row if we have reached the end of the current row
        if col == 9:
            return backtrack(row + 1, 0)

        # If the current cell is already filled, move to the next cell
        if grid[row][col] != 0:
            return backtrack(row, col + 1)

        # Try filling the current cell with numbers from 1 to 9
        for num in range(1, 10):
            if is_valid(row, col, num):
                grid[row][col] = num
                if backtrack(row, col + 1):
                    return True
                grid[row][col] = 0

        # If no valid number is found, backtrack
        return False

    # Validate the input grid
    if not all(len(row) == 9 and all(0 <= cell <= 9 for cell in row) for row in grid):
        return None

    # Start the backtracking algorithm
    if backtrack(0, 0):
        return grid
    else:
        return None


```

# Links
1. https://docs.anthropic.com/claude/page/function-fabricator