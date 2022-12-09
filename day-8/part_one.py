from typing import List


def tree_is_visible(grid: List[List[int]], row: int, col: int) -> bool:
    height = grid[row][col]
    grid_row = grid[row]

    if (max(grid_row[:col], default=-1) < height) or (max(grid_row[col + 1:], default=-1) < height):
        return True

    grid_col = [r[col] for r in grid]
    if (max(grid_col[:row], default=-1) < height) or (max(grid_col[row + 1:], default=-1) < height):
        return True

    return False


with open('input.txt') as input:
    grid = [[int(char) for char in line.strip()] for line in input]

    visible_trees = 0

    for row, grid_row in enumerate(grid):
        for col, tree in enumerate(grid_row):
            if tree_is_visible(grid, row, col):
                print("T", end="")
                visible_trees += 1
            else:
                print("_", end="")
        print("\n", end="")

    print("Visible trees", visible_trees)
