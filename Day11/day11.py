import sys
import string
from more_itertools import sliding_window
from itertools import groupby

infile = sys.argv[1] if len(sys.argv) > 1 else 'day11.txt'
# infile = sys.argv[1] if len(sys.argv) > 1 else 'day11test.txt'

# available = list(string.ascii_lowercase)

# C = sliding_window(available, 3)
# for c in C:
#     print(c)

letters = string.ascii_lowercase
# puzzle = "hepxcrrq"
puzzle = "hepxxyzz"
next_letter = {c1: c2 for c1, c2 in zip(letters, letters[1:]+'a')}
# print(next_letter)
# start at end of string - if its not 'z' increase its value
# if it is 'z' - make that value an 'a' and increase the value of the letter before it


def increase(pw):
    pw = pw[:-1] + next_letter[pw[-1]]
    for i in range(-1, -8, -1):
        if pw[i] == 'a':
            pw = pw[:i-1] + next_letter[pw[i-1]] + pw[i:]
        else:
            break
    return pw


    

    

    

    

def passes(pw):
    if pw == 'hepxxyzz':
        return False
    available = list(string.ascii_lowercase)
    C = sliding_window(available, 3)
    banned = ['i', 'o', 'l']
    doubles = [list(g) for k, g in groupby(pw)]
    good = False
    dc = 0
    for b in banned:
        if b in pw:
            return False
    for c in C:
        if ''.join(c) in pw:
            good = True
    for d in doubles:
        if len(d) > 1:
            dc += 1
    if dc > 1 and good:
        return True
    return False



while not passes(puzzle):
    puzzle = increase(puzzle)
print(puzzle)


# print(puzzle)
# print(increase(puzzle))
# print(passes("abcdffaa"))