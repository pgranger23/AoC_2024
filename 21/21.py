from functools import cache
from itertools import permutations

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    return list(map(str.strip, lines))

positions ={
    '7': (0,0),
    '8': (0,1),
    '9': (0,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '1': (2,0),
    '2': (2,1), 
    '3': (2,2),
    '0': (3,1), 
    'A': (3,2)  
}

grid_digicode ={
    '^': (0,1),
    'A': (0,2),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2)
}

grid_digicode_invalid = (3,0)
grid_robot_invalid = (0,0)

@cache
def get_all_valid_paths(start, end, invalid_idx):
    vertical_steps = end[0] - start[0]
    horizontal_steps = end[1] - start[1]

    moves = {'^': (-1,0),
             '<': (0,-1),
             '>': (0,1),
             'v': (1,0)}
    
    ud = '^' if vertical_steps < 0 else 'v'
    lr = '<' if horizontal_steps < 0 else '>'
    steps = [ud] * abs(vertical_steps) + [lr] * abs(horizontal_steps)

    unique_paths = set(permutations(steps))
    valid_paths = set()
    for path in unique_paths:
        cur_x, cur_y = start
        is_valid = True

        for move in path:
            dx,dy = moves[move]
            cur_x += dx
            cur_y += dy

            if (cur_x, cur_y) == invalid_idx:
                is_valid = False
                break
        
        if is_valid:
            valid_paths.add(path)

    return valid_paths

@cache
def solve_paths(paths, level, nlevels):
    cur_buttons = []
    for path in paths:
        path_buttons = 0
        for start, end, in zip(path, path[1:]):
                paths_local = get_all_valid_paths(grid_digicode[start], grid_digicode[end], grid_robot_invalid)
                if level == nlevels:
                    updated_paths_local = {p + ('A',) for p in paths_local} #Adding the final press
                    min_next_iter_buttons = min([len(p) for p in updated_paths_local])
                else:
                    updated_paths_local = {('A',) + p + ('A',) for p in paths_local} #Adding the presses
                    min_next_iter_buttons = solve_paths(frozenset(updated_paths_local), level + 1, nlevels)

                path_buttons += min_next_iter_buttons
            
        cur_buttons.append(path_buttons)

    buttons = min(cur_buttons) 
                
    return buttons


def process_code(code, nlevels):
    buttons = 0
    code =  'A' + code #Starting at "digit" A
    for start, end in zip(code, code[1:]):
        paths = get_all_valid_paths(positions[start], positions[end], grid_digicode_invalid)
        updated_paths = {('A',) + path + ('A',) for path in paths} #Adding the presses

        buttons += solve_paths(frozenset(updated_paths), 1, nlevels) #Using frozenset to make it hashable

    return buttons

codes = parse_input('21.input')

part1 = 0
part2 = 0 
for code in codes:
    value = int(code[:3])
    part1 += value*process_code(code, 2)
    part2 += value*process_code(code, 25)

print(f'Part1: {part1}')
print(f'Part2: {part2}')