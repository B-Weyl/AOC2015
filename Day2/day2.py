import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day2.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day2test.txt'
dimensions = open(infile).readlines()
part1 = 0
part2 = 0
for d in dimensions:
    l, w, h = [int(x) for x in d.split('x')]
    part1 += (2 * l * w) + (2 * w * h) + (2 * h * l)
    part1 += min((l * w), (w * h), (h * l))
    part2 += (l*w*h)
    part2 += min((2*l + 2*w), (2*w + 2*h), (2*h + 2*l))
    
print(part1)
print(part2)
