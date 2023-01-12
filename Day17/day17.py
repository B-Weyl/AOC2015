import sys
from itertools import combinations
from collections import Counter
infile = sys.argv[1] if len(sys.argv) > 1 else 'day17.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day17test.txt'

containers = [int(x) for x in open(infile).readlines()]
print(containers)

total = 0
container_lengths = []
# thankfully using itertools.combinations we do not need to
# account for multiples of the same values being used twice
# as that will be taken care of by generating all the possible combinations
# of any length
for x in range(2, len(containers)):
    c = combinations(containers, x)
    for cc in c:
        counts = Counter(cc)
        if sum(cc) == 150:
            total += 1
            container_lengths.append(len(cc))
        
# part 1        
print(total)
# part 2
cl_counts = Counter(container_lengths)
print(cl_counts[min(cl_counts.keys())])
            
