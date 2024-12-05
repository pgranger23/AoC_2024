import re

def read_input(fname):
    with open(fname) as f:
        data = f.read()
    return data

memory = read_input('3.input')

correct_values = re.findall(r'mul\((\d+),(\d+)\)', memory)
correct_values = [int(a)*int(b) for a, b in correct_values]
print("Total sum of correct values:", sum(correct_values))

#########Part 2#########
correct_values = re.findall(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))', memory)
activated = True
total = 0
for value in correct_values:
    if "don't" in value[0]:
        activated = False
    elif "do" in value[0]:
        activated = True
    else:
        if activated:
            total += int(value[1])*int(value[2])
print("Total sum of correct values with new rule:", total)