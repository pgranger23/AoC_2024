import re
import numpy as np
import sys
from PIL import Image
from tqdm import tqdm

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    data = []
    
    for line in lines:
        values = list(map(int, re.findall(r'(-*\d+)', line)))
        data.append(values)
    return data


def new_pos_after_nsteps(ns, pos, vel, mat_size):
    return ((pos[0] + ns*vel[0])%mat_size[0], (pos[1] + ns*vel[1])%mat_size[1])

robots = parse_input('14.input')

mat_size = (101, 103)
nsteps = 100

nb_robots_per_quadrant = [0, 0, 0, 0]

# mat = np.zeros(mat_size)

for robot in robots:
    pos = robot[:2]
    vel = robot[2:]
    new_pos = new_pos_after_nsteps(nsteps, pos, vel, mat_size)
    is_x_left = new_pos[0] < (mat_size[0] - 1)//2
    is_x_right = new_pos[0] > (mat_size[0] - 1)//2
    is_y_up = new_pos[1] < (mat_size[1] - 1)//2
    is_y_down = new_pos[1] > (mat_size[1] - 1)//2
    if is_x_left and is_y_up:
        nb_robots_per_quadrant[0] += 1
    elif is_x_right and is_y_up:
        nb_robots_per_quadrant[1] += 1
    elif is_x_left and is_y_down:
        nb_robots_per_quadrant[2] += 1
    elif is_x_right and is_y_down:
        nb_robots_per_quadrant[3] += 1

print(np.prod(nb_robots_per_quadrant))


### PART 2 ###
np.set_printoptions(threshold=sys.maxsize)
for nstep in tqdm(range(10000)):
    mat = np.zeros(mat_size)
    for robot in robots:
        pos = robot[:2]
        vel = robot[2:]
        new_pos = new_pos_after_nsteps(nstep, pos, vel, mat_size)
        mat[new_pos] += 1
    mat = mat > 0
    Image.fromarray((mat*255).astype(np.uint8)).save(f'images/14_{nstep}.png')

