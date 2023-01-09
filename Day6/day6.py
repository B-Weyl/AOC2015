import sys
import numpy as np
infile = sys.argv[1] if len(sys.argv) > 1 else 'day6.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day6test.txt'
GRID = [[0 for _ in range(1000)] for _ in range(1000)]
GRID2 = [[0 for _ in range(1000)] for _ in range(1000)]


instructions = open(infile).readlines()
for i in instructions:
    match i.split(' '):
        case "toggle", start, _, end:
            # print("toggling lights")
            startx, starty = [int(i) for i in start.split(',')]
            endx, endy = [int(i) for i in end.split(',')]
            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    # part 1 toggle
                    if GRID[x][y] == 1:
                        GRID[x][y] -= 1
                    else:
                        GRID[x][y] += 1
                    # part 2 toggle
                    GRID2[x][y] += 2
        case _, "on", start, _, end:
            # print("turning on lights")
            startx, starty = [int(i) for i in start.split(',')]
            endx, endy = [int(i) for i in end.split(',')]
            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    # part 1 on
                    GRID[x][y] = 1
                    # part 2 on
                    GRID2[x][y] += 1
        case _, "off", start, _, end:
            # print("turning off lights")
            startx, starty = [int(i) for i in start.split(',')]
            endx, endy = [int(i) for i in end.split(',')]
            for x in range(startx, endx + 1):
                for y in range(starty, endy + 1):
                    # part 1 off
                    GRID[x][y] = 0
                    # part 2 off
                    if GRID2[x][y] - 1 < 0:
                        GRID2[x][y] = 0
                    else:
                        GRID2[x][y] -= 1

part1 = 0
part2 = 0
for i in range(len(GRID)):
    for j in range(len(GRID[0])):
        if GRID[i][j] == 1:
            part1 += 1
for i in range(len(GRID2)):
    for j in range(len(GRID2[0])):
        part2 += GRID2[i][j]

print(part1, part2)

    

