import sys
from math import prod
infile = sys.argv[1] if len(sys.argv) > 1 else 'day15.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day15test.txt'

I =[]
CAP = []
DUR = []
FLAVOR = []
TEXTURE = []
CAL = []
ingredients = open(infile).readlines()
for i in ingredients:
    words = i.split()
    cap, dur, flavor, texture, cal = int(words[2][:-1]), int(words[4][:-1]), int(words[6][:-1]), int(words[8][:-1]), int(words[10])
    CAP.append(cap)
    DUR.append(dur)
    FLAVOR.append(flavor)
    TEXTURE.append(texture)
    CAL.append(cal)
    I.append((cap, dur, flavor, texture))

RL = []
for a in range(98):
    for b in range(98):
        for c in range(98):
            d = 100 - a - b - c
            if d > 0:
                RL.append((a, b, c, d))
# part 1
A = list(range(101))
B = list(reversed(list(range(101))))
C = list(zip(A, B))
R = []
CTOTAL = []
# example
for x in range(len(I) - 1):
    r  = []
    for a, b in C:
        cap_total = a * CAP[x] + b * CAP[x+1]
        dur_total = a * DUR[x] + b * DUR[x+1]
        f_total = a * FLAVOR[x] + b * FLAVOR[x+1]
        t_total = a * TEXTURE[x] + b * TEXTURE[x+1]
        if cap_total < 0 or dur_total < 0 or f_total < 0 or t_total < 0:
            R.append((0, 0, 0, 0))
        else:
            R.append(prod((cap_total, dur_total, f_total, t_total)))

for x in range(len(I) - 3):
    r  = []
    for a, b, c, d in RL:
        cap_total = a * CAP[x] + b * CAP[x+1] + c * CAP[x+2] + d * CAP[x+3]
        dur_total = a * DUR[x] + b * DUR[x+1] + c * DUR[x+2] + d * DUR[x+3]
        f_total = a * FLAVOR[x] + b * FLAVOR[x+1] + c * FLAVOR[x+2] + d * FLAVOR[x+3]
        t_total = a * TEXTURE[x] + b * TEXTURE[x+1] + c * TEXTURE[x+2] + d * TEXTURE[x+3]
        cal_total = a * CAL[x] + b * CAL[x+1] + c * CAL[x+2] + d * CAL[x+3]
        if cap_total < 0 or dur_total < 0 or f_total < 0 or t_total < 0:
            R.append((0, 0, 0, 0))
        else:
            R.append((cap_total, dur_total, f_total, t_total))
            if cal_total == 500:
                CTOTAL.append(prod((cap_total, dur_total, f_total, t_total)))

mmax = 0
for rr in R:    
    mmax = max(prod(rr), mmax)

# part 1
print(mmax)    
# part 2
print(max(CTOTAL))
        











    

