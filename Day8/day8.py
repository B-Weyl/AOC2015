code = 0
memory = 0

values = open('day8.txt').read()
if values[-1] == '\n':
    values = values[:-1]

lines = values.split('\n')
answer1 = 0
for l in lines:
    answer1 += len(l) - len(eval(l))

print(answer1)
answer2 = 0
for l in lines:
    answer2 += l.count('\\') + l.count('"') + 2
print(answer2)

