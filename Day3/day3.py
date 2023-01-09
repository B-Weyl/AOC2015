import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day3.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day3test.txt'
part1 = 1
SANTA = [0, 0]
ROBOT_SANTA = [0, 0]
santa_visited = set()
robot_visited = set()

moves = open(infile).read()
for i,m in enumerate(moves):
    santa_visited.add((SANTA[0], SANTA[1]))
    robot_visited.add((ROBOT_SANTA[0], ROBOT_SANTA[1]))
    if i % 2 == 0:
        match i,m:
            case _,'>':
                SANTA[0] += 1
            case _,'<':
                SANTA[0] -= 1
            case _,'^':
                SANTA[1] += 1
            case _,'v':
                SANTA[1] -= 1
    else:
        # robot_visited.add((SANTA[0], SANTA[1]))
        match i,m:
            case _,'>':
                ROBOT_SANTA[0] += 1
            case _,'<':
                ROBOT_SANTA[0] -= 1
            case _,'^':
                ROBOT_SANTA[1] += 1
            case _,'v':
                ROBOT_SANTA[1] -= 1

part1 = len(santa_visited)
print(part1)
part2 = len(santa_visited.union(robot_visited))
print(part2)
    


    

