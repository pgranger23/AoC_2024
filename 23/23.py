from itertools import combinations

def read_input(fname):
    with open(fname) as f:
        return [x.split('-') for x in f.read().splitlines()]
    
connections = read_input("23.input")

adjacency_list = {}
for connection in connections:
    a, b = connection
    if not a in adjacency_list:
        adjacency_list[a] = []
    adjacency_list[a].append(b)
    if not b in adjacency_list:
        adjacency_list[b] = []
    adjacency_list[b].append(a)

valid_sets = set()

for node, neighbors in adjacency_list.items():
    if node[0] != 't':
        continue
    for a, b in combinations(neighbors, 2):
        if a in adjacency_list[b]:
            valid_sets.add(frozenset([node, a, b]))

print("Part 1:", len(valid_sets))



####Part 2####

max_clique = set()

def find_subgraphs(R, P, X):
    if not P and not X:
        global max_clique
        if len(R) > len(max_clique):
            max_clique = R
        return
    for v in P.copy():
        find_subgraphs(R.union({v}), P.intersection(adjacency_list[v]), X.intersection(adjacency_list[v]))
        P.remove(v)
        X.add(v)

find_subgraphs(set(), set(adjacency_list.keys()), set())

print("Part 2:", ','.join(sorted(list(max_clique))))

# for node, neighbors in adjacency_list.items():
#     current_set = set(neighbors)
#     current_set.add(node)
#     for n in neighbors:
#         current_set = current_set.intersection(adjacency_list[n] + [n])
#     print(node, current_set)
