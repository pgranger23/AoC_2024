import numpy as np
from itertools import product

def parse_input(fname):
    with open(fname) as f:
        lines = f.read().splitlines()

    assert(len(lines)%8 == 7)
    n_patterns = (len(lines) + 1)//8
    patterns = [np.array([list(x) for x in lines[i*8:i*8+7]]) for i in range(n_patterns)]
    return patterns

def get_sequence(pattern):
    return np.count_nonzero(pattern == '#', axis=0) - 1

patterns = parse_input("25.input")
keys = []
locks = []
for pattern in patterns:
    if(np.count_nonzero(pattern[0] == '#') == pattern.shape[1]):
        locks.append(pattern)
    else:
        keys.append(pattern)

keys_seq = [get_sequence(x) for x in keys]
locks_seq = [get_sequence(x) for x in locks]

nb_fitting = 0
for k, l in product(keys_seq, locks_seq):
    if np.count_nonzero(k + l > 5) == 0:
        nb_fitting += 1

print("Part 1:", nb_fitting)
