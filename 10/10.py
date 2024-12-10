import numpy as np

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    
    return np.array([list(map(int, line.strip())) for line in lines])

mat = parse_input('10.input')

starts = np.argwhere(mat == 0)
paths = np.hstack((starts, starts, np.zeros((len(starts), 1), dtype=int))).tolist()

good_paths = []

while paths:
    path = paths.pop()
    if path[-1] == 9:
        good_paths.append(path)
        continue
    for i, j in ((path[0] + 1, path[1]), (path[0] - 1, path[1]), (path[0], path[1] - 1), (path[0], path[1] + 1)):
        if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
            continue
        if mat[i, j] == path[-1] + 1:
            paths.append([i, j, path[2], path[3], path[-1] + 1])

nb_unique_paths = len(np.unique(good_paths, axis=0))

print("Number of unique paths:", nb_unique_paths)


#####Part 2#####

print("Number of paths:", len(good_paths))