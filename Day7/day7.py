from collections import defaultdict
directions = open('day7.txt').readlines()
# new_directions = sorted(directions, key=len)
# print(new_directions)
print(directions)
signals = defaultdict(int)



for direction in directions:
    d = direction.split(' ')
    print(d)
    if len(d) == 3:
        if d[0] in signals.keys():
            signals[d[2].strip()] = signals[d[0]]
        else:
            signals[d[2].strip()] = int(signals[d[0]])

        signals[d[2].strip()] = int(d[0])
    elif len(d) == 5:
        match d[1]:
            case 'AND':
                signals[d[4]] = signals[d[0]] & signals[d[2]]
            case 'OR':
                signals[d[4]] = signals[d[0]] | signals[d[2]]
            case 'LSHIFT':
                signals[d[4]] = signals[d[0]] << int(d[2])
            case 'RSHIFT':
                signals[d[4]] = signals[d[0]] >> int(d[2])
    elif len(d) == 4:
        # z = signals[d[1]]
        # l = len(str(z))
        # bv = ((5 - l) * '0') + str(z)
        # k = bin(int(bv))

        # signals[d[3]] = ~int(bv)
        signals[d[3]] = 65535 - (signals[d[1]])

print(signals.items())