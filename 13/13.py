import re
def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()

    data = []
    
    for i in range(0, len(lines), 4):
        button_a = list(map(int, re.findall(r'(\d+)', lines[i])))
        button_b = list(map(int, re.findall(r'(\d+)', lines[i+1])))
        prize = list(map(int, re.findall(r'(\d+)', lines[i+2])))
        data.append((button_a, button_b, prize))
    return data

def get_solution(button_a, button_b, prize):
    a = button_a[0]
    b = button_b[0]
    c = prize[0]
    alpha = button_a[1]
    beta = button_b[1]
    gamma = prize[1]

    if alpha*b - beta*a != 0: #Single solution
        if (alpha*c - a*gamma)%(alpha*b - beta*a) == 0: #integer solution
            y = (alpha*c - a*gamma)/(alpha*b - beta*a)
            x = (c - b*y)/a
            if x == int(x):
                return x, y
        return None, None
    
    if alpha*c - gamma*a != 0:
        return None, None
    
    #Case with many solutions, not in input apparently
    return None

data = parse_input('13.input')

score = 0
for button_a, button_b, prize in data:
    solution = get_solution(button_a, button_b, prize)
    assert(solution != None)
    if solution[0] != None:
        score += solution[0]*3 + solution[1]
print("Score:", score)

#####Part 2#####
score = 0
for button_a, button_b, prize in data:
    prize[0] += 10000000000000
    prize[1] += 10000000000000
    solution = get_solution(button_a, button_b, prize)
    assert(solution != None)
    if solution[0] != None:
        score += solution[0]*3 + solution[1]
print("Score:", score)
