import sys
from hashlib import md5
infile = sys.argv[1] if len(sys.argv) > 1 else 'day3.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day3test.txt'

key = "bgvyzdsv"
found = False
for x in range(6_000_000):
    test = key + str(x)
    # print(test)
    ans = md5(test.encode())
    A = ans.hexdigest()
    if A[:5] == '00000' and not found:
        part1 = x
        found = True
    if A[:6] == '000000':
        part2 = x
        break
print(part1, part2)
        
        

