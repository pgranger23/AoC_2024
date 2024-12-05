def parse_input(fname):
    with open(fname) as f:
        data = f.read().splitlines()
    data = [data.split(' ') for data in data]
    first_list = list(map(int, [elt[0] for elt in data]))
    second_list = list(map(int, [elt[-1] for elt in data]))
    return first_list, second_list

L1, L2 = parse_input('1.input')

L1 = sorted(L1)
L2 = sorted(L2)

distance = 0
for i in range(len(L1)):
    distance += abs(L1[i] - L2[i])
print("Distance:", distance)

########Part 2########

similarity = 0
for elt in L1:
    similarity += elt*L2.count(elt)
print("Similarity:", similarity)