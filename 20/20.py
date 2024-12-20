import numpy as np
from itertools import combinations

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    maze = np.char.array([list(line.strip()) for line in lines])
    return maze

maze = parse_input('20.input')

S = np.argwhere(maze == 'S')[0]
start = (S[0] + S[1]*1j)

dist = {start: 0}
to_check = [start]
while to_check:
    pos = to_check.pop()
    for new_pos in pos - 1, pos + 1, pos - 1j, pos + 1j:
        if maze[int(new_pos.real), int(new_pos.imag)] != '#' and new_pos not in dist:
            dist[new_pos] = dist[pos] + 1
            to_check.append(new_pos)

nb_part1 = 0
nb_part2 = 0

for (p,i), (q,j) in combinations(dist.items(), 2):
    d = abs((p-q).real) + abs((p-q).imag)
    if d == 2 and j-i-d >= 100: nb_part1 += 1
    if d < 21 and j-i-d >= 100: nb_part2 += 1

print("Part 1:", nb_part1)
print("Part 2:", nb_part2)