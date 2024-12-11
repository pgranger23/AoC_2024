from math import log10

def parse_input(fname):
    with open(fname) as f:
        values = list(map(int, f.read().strip('\n').split(' ')))
    
    return values

def evolve(value):
    if value == 0:
        return [1]
    nb_digits = int(log10(value)) + 1
    if nb_digits%2 == 0: #Even number og digits
        return [value//(10**(nb_digits//2)), value%(10**(nb_digits//2))]
    return [value*2024]

values = parse_input('11.input')
values = {value: 1 for value in values}

for i in range(75):
    new_values = {}
    for value, count in values.items():
        evolved = evolve(value)
        for value in evolved:
            if value in new_values:
                new_values[value] += count
            else:
                new_values[value] = count
    
    values = new_values
    if i == 24:
        values_25 = values
print(sum(values_25.values()))
print(sum(values.values()))