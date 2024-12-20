from functools import cache
def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    towels = tuple([line.strip() for line in lines[0].split(',')])

    patterns = [line.strip('\n') for line in lines[2:]]

    return towels, patterns

def is_pattern_possible(pattern, towels):
    longest_towel = max(map(len, towels))
    current_patterns = [pattern]
    while current_patterns:
        current_pattern = current_patterns.pop()
        if not current_pattern:
            return True
        for i in range(1, longest_towel + 1):
            if current_pattern[:i] in towels:
                new_pattern = current_pattern[i:]
                current_patterns.append(new_pattern)
    return False

@cache
def nb_possibilities(pattern, towels):
    longest_towel = max(map(len, towels))
    if not pattern:
        return 1
    total = 0
    for i in range(1, longest_towel + 1):
        if i > len(pattern):
            break
        if pattern[:i] in towels:
            new_pattern = pattern[i:]
            total += nb_possibilities(new_pattern, towels)
    return total
    

towels, patterns = parse_input('19.input')

nb_possible = 0
for pattern in patterns:
    if is_pattern_possible(pattern, towels):
        nb_possible += 1

print("Number of possible patterns:", nb_possible)

####Part 2####

nb_possible = 0
for pattern in patterns:
    nb_possible += nb_possibilities(pattern, towels)
print("Number of possible arrangements:", nb_possible)