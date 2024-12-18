import numpy as np
import heapq
def parse_input(file, size=71):
    with open(file) as f:
        locations = np.array([list(map(int, line.split(','))) for line in f])
    mat = np.zeros((size, size), dtype=np.uint16)
    for num, (i, j) in enumerate(locations):
        mat[i, j] = num + 1
    return mat

def find_path(mat):
    paths = []
    paths.append((0, 0, 0))
    stop_i, stop_j = mat.shape[0] - 1, mat.shape[1] - 1

    visited = set()

    while paths:
        path = heapq.heappop(paths)        
        if (path[1], path[2]) in visited:
            continue

        visited.add((path[1], path[2]))

        if path[1] == stop_i and path[2] == stop_j:
            return path[0]

        for direc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            i, j = path[1] + direc[0], path[2] + direc[1]
            if i < 0 or j < 0 or i >= mat.shape[0] or j >= mat.shape[1]:
                continue
            if mat[i, j] != True:
                continue
            neighbor = (path[0] + 1, i, j)
            heapq.heappush(paths, neighbor)

mat = parse_input('18.input', 71)
distance = find_path((mat == 0)| (mat > 1024))
print("Distance to target:", distance)

####Part 2####
nb_bytes = 1024
max_nb_bytes = np.max(mat)

low = 1024
high = max_nb_bytes
while low < high:
    mid = (low + high) // 2
    if find_path((mat == 0)| (mat > mid)):
        low = mid + 1
    else:
        high = mid

print("First blockin byte:", ','.join(map(str, np.argwhere(mat == low).tolist()[0])))