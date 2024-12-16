import numpy as np
def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    maze = np.char.array([list(line.strip()) for line in lines])
    return maze

def get_neighbours(pos):
    return [
        ((pos[0] + pos[1], pos[1]), 1),
        ((pos[0], pos[1] * 1j), 1000),
        ((pos[0], -pos[1]*1j), 1000),
    ]

maze = parse_input('16.input')

S = np.argwhere(maze == 'S')[0]
pos = (S[0] + 1j*S[1], 1j)

E = np.argwhere(maze == 'E')[0]
target = (E[0] + 1j*E[1])

distance_map = {pos: 0}
predecessor_map = {pos: [None]}

to_visit = [pos]

while to_visit:
    current = to_visit.pop(0)
    for neighbour, add_score in get_neighbours(current):
        if maze[int(neighbour[0].real), int(neighbour[0].imag)] == '#':
            continue
        if neighbour not in distance_map:
            distance_map[neighbour] = distance_map[current] + add_score
            predecessor_map[neighbour] = [current]
            to_visit.append(neighbour)
        elif distance_map[current] + add_score < distance_map[neighbour]:
            distance_map[neighbour] = distance_map[current] + add_score
            predecessor_map[neighbour] =[current]
            to_visit.append(neighbour)
        elif distance_map[current] + add_score == distance_map[neighbour]:
            predecessor_map[neighbour] = predecessor_map.get(neighbour, []) + [current]

final_distance, actual_end = min([(distance_map[(loc, orientation)], (loc, orientation)) for loc, orientation in distance_map if loc == target])
print("Distance to target:", final_distance)

tiles_on_path = set()
to_backtrack = [actual_end]
while to_backtrack:
    current = to_backtrack.pop()
    tiles_on_path.add(current[0])
    for predecessor in predecessor_map[current]:
        if predecessor:
            to_backtrack.append(predecessor)

print("Number of tiles on path:", len(tiles_on_path))