import sys
infile = sys.argv[1] if len(sys.argv) > 1 else 'day14.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day14test.txt'

# part 1
T = []
reindeers = open(infile).readlines()
for reindeer in reindeers:
    total = 0
    words = reindeer.split()
    r, velocity, duration, rest = words[0], int(words[3]), int(words[6]), int(words[-2])
    for t in range(2503):
        if t % (duration + rest) < duration:
            total += velocity
    T.append(total) 
print(max(T))

# part 2
R = []
reindeers = open(infile).readlines()
for reindeer in reindeers:
    words = reindeer.split()
    r, velocity, duration, rest = words[0], int(words[3]), int(words[6]), int(words[-2])
    R.append((r, velocity, duration, rest))
VELS = [0] * len(R)
SCORES = [0] * len(R)
sec = 0
while sec < 2503:
    for x in range(len(R)):
        if sec % (R[x][2] + R[x][3]) < R[x][2]:
            VELS[x] += R[x][1]
    mv = max(VELS)
    for v in range(len(VELS)):
        if VELS[v] == mv:
            SCORES[v] += 1
    sec += 1

print(max(SCORES))  







    


        




    
    
    

    

        









