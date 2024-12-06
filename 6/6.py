import numpy as np
from tqdm import tqdm

def read_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    lines = [list(line.strip()) for line in lines]
    return np.array(lines)

arr = read_input('6.input')
start_pos = np.argwhere(arr == '^')[0]

obstacles = np.argwhere(arr == '#')
nrows, ncols = arr.shape

pos = start_pos[0] + start_pos[1]*1j
obstacles = set([obstacle[0] + obstacle[1]*1j for obstacle in obstacles])

def get_visited(pos, obstacles):
    direction = -1
    visited = set()
    visited_with_direction = set()
    loop = False
    while pos.real >= 0 and pos.imag >= 0 and pos.real < nrows and pos.imag < ncols:
        if (pos, direction) in visited_with_direction:
            loop = True
            break
        if pos in obstacles:
            pos -= direction
            direction = direction * (-1j)
        else:
            visited.add(pos)
            visited_with_direction.add((pos, direction))
            pos += direction
    return visited, loop

visited, loop = get_visited(pos, obstacles)

print("Number of visited positions:", len(visited))

##Stupid bruteforce solution...

nb_loops = 0
for new_obstacle in tqdm(visited):
    new_obstacles = obstacles | {new_obstacle}
    _, loop = get_visited(pos, new_obstacles)
    if loop:
        nb_loops += 1

print("Number of loops:", nb_loops)

##Start attempt at some smarter solution. But unecessary...

# obstacles_per_line = {}
# obstacles_per_column = {}
# for obstacle in obstacles:
#     if obstacle[0] not in obstacles_per_line:
#         obstacles_per_line[obstacle[0]] = [obstacle[1]]
#     else:
#         obstacles_per_line[obstacle[0]].append(obstacle[1])
#     if obstacle[1] not in obstacles_per_column:
#         obstacles_per_column[obstacle[1]] = [obstacle[0]]
#     else:
#         obstacles_per_column[obstacle[1]].append(obstacle[0])

# obstacles_per_line = {k: sorted(v) for k, v in obstacles_per_line.items()}
# obstacles_per_column = {k: sorted(v) for k, v in obstacles_per_column.items()}

# direction = -1j
# pos = start_pos[0] + start_pos[1]*1j
# visited = set([pos])

# while True:
#     if direction.imag > direction.real:
#         if pos.imag in obstacles_per_column:

#         index = np.searchsorted(obstacles_per_column[], )
#     if direction.real < -1 or direction.imag < -1:
#         comparison = np.le

#     direction = direction * (-1j)