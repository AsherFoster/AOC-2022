from typing import List


def dist(row: List[int], cap: int) -> int:
    for i, height in enumerate(row):
        if height >= cap:
            return i + 1

    return len(row)


def score_tree(grid: List[List[int]], row: int, col: int) -> int:
    height = grid[row][col]
    grid_row = grid[row]

    left = dist(list(reversed(grid_row[:col])), height)
    right = dist(grid_row[col + 1:], height)

    grid_col = [r[col] for r in grid]
    up = dist(list(reversed(grid_col[:row])), height)
    down = dist(grid_col[row + 1:], height)

    return left * right * up * down

with open('input.txt') as input:
    grid = [[int(char) for char in line.strip()] for line in input]

    tree_scores = max(score_tree(grid, y, x) for y, row in enumerate(grid) for x in range(0, len(row)))

    print("Max score", tree_scores)
