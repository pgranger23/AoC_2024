import numpy as np

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    
    return np.array([list(line.strip()) for line in lines])

def flood_fill(mat, start):
    value = mat[int(start.real), int(start.imag)]
    to_visit = set([start])
    visited = set()
    borders = set()
    while to_visit:
        node = to_visit.pop()
        visited.add(node)
        for i, j in ((node.real + 1, node.imag), (node.real - 1, node.imag), (node.real, node.imag - 1), (node.real, node.imag + 1)):
            if i < 0 or j < 0 or i >= len(mat[0]) or j >= len(mat):
                borders.add((node, i + j*1j - node))
                continue
            if mat[int(i), int(j)] == value:
                if i + j*1j not in visited:
                    to_visit.add(i + j*1j)
            else:
                borders.add((node, i + j*1j - node))
    return visited, borders

def count_borders(borders):
    #Only need to look at horizontal borders and multiply by 2
    horiz_borders = [border for border in borders if abs(border[1].real) == 1]
    horiz_borders = sorted(horiz_borders, key=lambda x: (x[1].real, x[0].real, x[0].imag))
    nb_matching_borders = 0
    for i in range(len(horiz_borders) - 1):
        if horiz_borders[i + 1][0] - horiz_borders[i][0] == 1j and horiz_borders[i + 1][1] == horiz_borders[i][1]:
            nb_matching_borders += 1
    return (len(horiz_borders) - nb_matching_borders)*2
    


mat = parse_input('12.input')
to_visit = set([m + n*1j for m in range(len(mat[0])) for n in range(len(mat))])
score = 0
while to_visit:
    start = to_visit.pop()
    visited, borders = flood_fill(mat, start)
    to_visit = to_visit - visited
    score += len(visited)*count_borders(borders)
    
print("Score:", score)

