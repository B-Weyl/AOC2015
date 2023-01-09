import sys
from itertools import groupby
from itertools import pairwise
from itertools import zip_longest
infile = sys.argv[1] if len(sys.argv) > 1 else 'day5.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day5test.txt'
part1 = 0
part2 = 0
S = open(infile).readlines()
vowels = ['a', 'e', 'i', 'o', 'u']
banned = ['ab', 'cd', 'pq', 'xy']
for s in S:
    good_groups = False
    groups = [list(g) for k, g in groupby(s)]
    for g in groups:
        if len(g) > 1:
            good_groups = True
    nvowels = sum([v in vowels for v in s])
    good_banned = True
    for b in banned:
        if b in s:
            good_banned = False
    if good_banned and nvowels >= 3 and good_groups:
        part1 += 1
# part 2
for s in S:
    s = list(s.strip())
    good_pair = False
    for z in range(len(s) - 1):
        pair = s[z] + s[z+1]
        if pair in ''.join(s[z+2:]):
            good_pair = True
    good_pattern = False
    if len(s) > 3:
        for x in range(len(s) - 2):
            if s[x] == s[x+2]:
                good_pattern = True
    if good_pair and good_pattern:
        part2 += 1
print(part1)
print(part2)
            

