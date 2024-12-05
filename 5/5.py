from functools import cmp_to_key

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    separator = lines.index('')

    rules = [list(map(int, line.split('|'))) for line in lines[:separator]]
    pages = [list(map(int, line.split(','))) for line in lines[separator+1:]]

    return rules, pages

rules, pages = parse_input('5.input')

rules_dict = {}
for rule in rules:
    if rule[0] not in rules_dict:
        rules_dict[rule[0]] = [rule[1]]
    else:
        rules_dict[rule[0]].append(rule[1])

def get_page_list_value(page_list, rules_dict):
    for i in range(len(page_list)):
        for j in range(i+1, len(page_list)):
            if page_list[j] in rules_dict and page_list[i] in rules_dict[page_list[j]]:
                return 0
    return page_list[len(page_list)//2]

total_sum = 0
sum_2 = 0



def comparison(x, y):
    if x in rules_dict and y in rules_dict[x]:
        return -1
    elif y in rules_dict and x in rules_dict[y]:
        return 1
    else:
        return 0

for page_list in pages:
    value = get_page_list_value(page_list, rules_dict)
    total_sum += value
    if value ==0:
        sorted_list = sorted(page_list, key=cmp_to_key(comparison))
        sum_2 += sorted_list[len(sorted_list)//2]

print("Total sum:", total_sum)
print("Sum 2:", sum_2)
