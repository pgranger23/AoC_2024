def parse_input(fname):
    with open(fname) as f:
        data = f.read().splitlines()
    data = [list(map(int, data.split(' '))) for data in data]
    return data

def is_valid(report):
    diff = report[1] - report[0]
    for i in range(1, len(report)):
        new_diff = report[i] - report[i-1]
        if abs(new_diff) > 3 or new_diff == 0:
            return False
        if new_diff*diff < 0:
            return False
    return True

def problem_location(report):
    diff = report[1] - report[0]
    for i in range(1, len(report)):
        new_diff = report[i] - report[i-1]
        if abs(new_diff) > 3 or new_diff == 0:
            return i - 1
        if new_diff*diff < 0:
            return i -1
    return -1
        

reports = parse_input('2.input')

count = 0

for report in reports:
    count += is_valid(report)

print("Number of valid reports:", count)

count = 0

for report in reports:
    loc = problem_location(report)
    if loc == -1:
        count += 1
    else:
        trial0 = report[1:]
        trial1 = report[:loc] + report[loc+1:]
        trial2 = report[:loc+1] + report[loc+2:]
        if problem_location(trial0) == -1 or problem_location(trial1) == -1 or problem_location(trial2) == -1:
            count += 1

print("Number of valid reports with new rule:", count)