import numpy as np
def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    
    return np.array([list(line.strip()) for line in lines])

mat = parse_input('8.input')

chars = list(np.unique(mat))
chars.remove('.')  

max_i, max_j = np.array(mat.shape) - np.array((1, 1))

antinodes = set()

for ch in chars:
    locs = np.argwhere(mat == ch)
    locs = locs[..., 0] + locs[..., 1]*1j
    for i in range(len(locs)):
        for j in range(i+1, len(locs)):
            dist = locs[i] - locs[j]
            antinodes.add(locs[i] + dist)
            antinodes.add(locs[j] - dist)

antinodes = [i for i in antinodes if i.real >= 0 and i.imag >= 0 and i.real <= max_i and i.imag <= max_j]

print("Number of antinodes:", len(antinodes))


#####Part 2#####

antinodes = set()

def is_in_bounds(pos):
    return pos.real >= 0 and pos.imag >= 0 and pos.real <= max_i and pos.imag <= max_j

for ch in chars:
    locs = np.argwhere(mat == ch)
    locs = locs[..., 0] + locs[..., 1]*1j
    for i in range(len(locs)):
        for j in range(i+1, len(locs)):
            dist = locs[i] - locs[j]
            k = 0
            while is_in_bounds(locs[i] + k*dist):
                antinodes.add(locs[i] + k*dist)
                k += 1
            k = 1
            while is_in_bounds(locs[i] - k*dist):
                antinodes.add(locs[i] - k*dist)
                k += 1


print("Number of new antinodes:", len(antinodes))