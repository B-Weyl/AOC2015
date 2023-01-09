import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day1.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day1test.txt'
moves = open(infile).read()
ans1 = 0
ans2 = 0
found = False
for x in range(len(moves)):
    if moves[x] == '(':
        ans1 += 1
    else:
        ans1 -= 1
    if ans1 < 0 and not found:
        found = True
        ans2 = x
print(ans1)
print(ans2)


