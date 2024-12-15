import numpy as np

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip('\n') for line in lines]

    split = lines.index('')

    box_nb = 0
    mat = []
    mat2 = []
    for line in lines[:split]:
        new_line = []
        new_line2 = []
        for char in line:
            if char == '#':
                new_line += ['#']
                new_line2 += ['#', '#']
            elif char == '.':
                new_line += ['.']
                new_line2 += ['.', '.']
            elif char == '@':
                new_line += ['@']
                new_line2 += ['@', '.']
            else:
                new_line += [box_nb]
                new_line2 += [box_nb, box_nb]
                box_nb +=1

        mat.append(new_line)
        mat2.append(new_line2)
    mat = np.array(mat)
    mat2 = np.array(mat2)

    directions = []
    for line in lines[split+1:]:
        directions += line
    
    return mat, mat2, directions

def rotate_pos_90(k, pos, shape):
    if k == -1:
        return (pos[1], shape[1] - 1 - pos[0])
    elif k == -3:
        return (shape[0] - 1 - pos[1], pos[0])
    elif k == 1:
        return (shape[1] - 1 - pos[1], pos[0])
    elif k == 2 or k == -2:
        return (shape[0] - 1 - pos[0], shape[1] - 1 - pos[1])
    elif k == 3:
        return(pos[1], shape[0] - 1 - pos[0])
    elif k == 0:
        return pos

def score(mat):
    score = 0
    for i, line in enumerate(mat):
        unique = np.unique(line)
        for box in unique:
            if box == '.' or box == '#':
                continue
            score += i*100 + np.argmax(line == box)
    return score

def process_direction(mat, directions):
    cur_pos = np.argwhere(mat == '@')[0]
    mat[cur_pos[0], cur_pos[1]] = '.'
    rot_map = {'^': 3, 'v': 1, '<': 2, '>': 0}
    for direc in directions:
        nb_rot = rot_map[direc]


        rot_mat = np.rot90(mat, nb_rot)
        local_pos = rotate_pos_90(nb_rot, cur_pos, mat.shape)

        local_pos = (local_pos[0], local_pos[1] + 1)

        if rot_mat[local_pos[0], local_pos[1]] == '.':
            cur_pos = rotate_pos_90(-nb_rot, local_pos, mat.shape)
            continue
        if rot_mat[local_pos[0], local_pos[1]] == '#':
            continue

        #Check if the current box is in multiple parts
        to_move = set((local_pos,))
        if rot_mat[local_pos[0] - 1, local_pos[1]] == rot_mat[local_pos[0], local_pos[1]]:
            to_move.add((local_pos[0] - 1, local_pos[1]))
        elif rot_mat[local_pos[0] + 1, local_pos[1]] == rot_mat[local_pos[0], local_pos[1]]:
            to_move.add((local_pos[0] + 1, local_pos[1]))
        
        can_move = True
        to_check = set(to_move)
        while to_check:
            pos_to_shift = to_check.pop()
            if rot_mat[pos_to_shift[0], pos_to_shift[1] + 1] == '#':
                can_move = False
                break
            elif rot_mat[pos_to_shift[0], pos_to_shift[1] + 1] == '.':
                continue
            else:
                to_move.add((pos_to_shift[0], pos_to_shift[1] + 1,))
                to_check.add((pos_to_shift[0], pos_to_shift[1] + 1,))
                if rot_mat[pos_to_shift[0] - 1, pos_to_shift[1] + 1] == rot_mat[pos_to_shift[0], pos_to_shift[1] + 1]:
                    to_check.add((pos_to_shift[0] - 1, pos_to_shift[1] + 1))
                    to_move.add((pos_to_shift[0] - 1, pos_to_shift[1] + 1))
                elif rot_mat[pos_to_shift[0] + 1, pos_to_shift[1] + 1] == rot_mat[pos_to_shift[0], pos_to_shift[1] + 1]:
                    to_check.add((pos_to_shift[0] + 1, pos_to_shift[1] + 1))
                    to_move.add((pos_to_shift[0] + 1, pos_to_shift[1] + 1))
        if can_move:
            sorted_blocks = sorted(to_move, key=lambda x: x[1], reverse=True)
            for block_pos in sorted_blocks:
                rot_mat[block_pos[0], block_pos[1] + 1] = rot_mat[block_pos[0], block_pos[1]]
                rot_mat[block_pos[0], block_pos[1]] = '.'
            cur_pos = rotate_pos_90(-nb_rot, local_pos, mat.shape)       


mat, mat2, directions = parse_input('15.input')

process_direction(mat, directions)

print("Score is:", score(mat))

###Part 2###
process_direction(mat2, directions)
print("Score is:", score(mat2))