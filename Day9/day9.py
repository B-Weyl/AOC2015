import sys
from typing import Tuple
from itertools import permutations
infile = sys.argv[1] if len(sys.argv) > 1 else 'day9.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day9test.txt'

routes = open(infile).readlines()
T = {}
TOWNS = set()

for route in routes:
    words = route.split(' ')
    source, dest, amt = words[0], words[2], int(words[-1].strip())
    T[tuple[source, dest]] = amt
    TOWNS.add(source)
    TOWNS.add(dest)

E = list(TOWNS)
S = []
everyRoute = list(permutations(E))
for x in range(len(everyRoute) - 1):
    total = 0
    for y in range(len(everyRoute[0]) - 1):
        try:
            total += T[tuple[everyRoute[x][y], everyRoute[x][y+1]]]
        except:
             total += T[tuple[everyRoute[x][y+1], everyRoute[x][y]]]
    S.append(total)

print(min(S))
print(max(S))






            


    













