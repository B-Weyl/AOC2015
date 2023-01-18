import sys
from copy import deepcopy
from itertools import product
infile = sys.argv[1] if len(sys.argv) > 1 else 'day18.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day18test.txt'

# there is a very good write up found at :
# https://www.reddit.com/r/adventofcode/comments/zkc974/python_data_structures_for_2d_grids/
# for multiple ways to do 2d grids and neighbors.
# i personally liked the dictionary method


grid = {(x, y): val.strip() for y, line in enumerate(open(infile).readlines())
        for x, val in enumerate(line)}
new_grid = deepcopy(grid)

# four corners are (0, 0), (99, 0), (0, 99), and (99, 99)


def neighbors(grid, pos):
    total = 0
    x0, y0 = pos
    candidates = [(x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1), (x0 - 1, y0 - 1), (x0 + 1, y0 + 1), (x0 - 1, y0 + 1), (x0 + 1, y0 - 1)]
    for c in candidates:
        if c in grid:
            if grid[c] == '#':
                total += 1
    return total

x = 0
#comment out the hardcoding corners logic for answer in part 1
for p in [(0, 0), (99, 0), (0, 99), (99, 99)]:
    grid[p] = '#'
while x < 100:
    for point in grid.keys():
        if grid[point] == '#':
            if neighbors(grid, point) == 2 or neighbors(grid, point) == 3:
                new_grid[point] = '#'
            else:
                new_grid[point] = '.'
        if grid[point] == '.':
            if neighbors(grid, point) == 3:
                new_grid[point] = '#'
            else:
                new_grid[point] = '.'
    grid = deepcopy(new_grid)
    x += 1

part1 = 0
part2 = 0
for v in grid.values():
    if v == '#':
        part1 += 1
print(part1)




