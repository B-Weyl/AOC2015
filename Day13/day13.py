import sys
from itertools import permutations  
infile = sys.argv[1] if len(sys.argv) > 1 else 'day13.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day13test.txt'


G = dict()
people = set()
seats = open(infile).readlines()
for seat in seats:
    words = seat.split()
    print(words)
    pairs = tuple((words[0], words[-1][:-1]))
    amt = int(words[3])
    people.add(words[0])
    match words[2]:
        case 'gain':
            G[pairs] = amt
        case 'lose':
            G[pairs] = -amt
# if part 2 - add yourself into the group of people
# people.add('Me')

print(G)
options = permutations(people, len(people))

totals = []
total = 0
for o in options:
    total = 0
    for p in range(len(o)):
        adj = (p + 1) % len(o)
        # logic for part 2
        if 'Me' in (o[p], o[adj]):
            continue
        print(o[p], o[adj])
        total += G[o[p], o[adj]]
    for q in range(len(o)):
        adj = (q - 1) % len(o)
        # logic for part 2
        if 'Me' in (o[q], o[adj]):
            continue
        total += G[o[q], o[adj]]
    totals.append(total)
print(max(totals))



        
    


    