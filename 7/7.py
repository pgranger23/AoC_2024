def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    lines = [line.strip().split(': ') for line in lines]
    lines = [[int(line[0]), list(map(int, line[1].split(' ')))] for line in lines]
    return lines

def is_valid(target, numbers, part=1):
    if len(numbers) == 0:
        return target == 0
    next_number = numbers[-1]

    if target%next_number == 0:
        if is_valid(target//next_number, numbers[:-1], part=part):
            return True
    if target-next_number >= 0:
        if is_valid(target-next_number, numbers[:-1], part=part):
            return True
    if part == 2:
            if (target - next_number)%(10**(len(str(next_number)))) == 0:
                if is_valid((target - next_number)//(10**(len(str(next_number)))), numbers[:-1], part=part):
                    return True

equations = parse_input('7.input')
total = 0
for equation in equations:
    if is_valid(*equation):
        total += equation[0]

print("Total:", total)


#####Part 2#####

total = 0
for equation in equations:
    if is_valid(*equation, part=2):
        total += equation[0]

print("Total part2:", total)
