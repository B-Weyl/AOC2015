import sys
from collections import Counter
infile = sys.argv[1] if len(sys.argv) > 1 else 'day10.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day10test.txt'

puzzle = "3113322113"
p = "111221"
ROUNDS = 40

# break into groups of repeated numbers
def separate(value, rounds):
    while rounds > 0:
        A = []
        prev = ""
        ans = ""
        for v in value:
            if v == prev:
                ans += v
            else:
                A.append(ans)
                prev = v
                ans = v
        A.append(ans) 
        B = []
        r = rounds - 1
        for a in A[1:]:
            b = []
            b.append(str(a.count(a[0])))
            b.append(a[0])
            B.append(b)
        C = ''.join([item for sublist in B for item in sublist])
        return separate(C, r)
    return len(value)

# gross brute force, but it works
print(separate(puzzle, 40))
print(separate(puzzle, 50))









    





        

        
        







