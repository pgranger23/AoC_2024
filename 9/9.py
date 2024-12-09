from dataclasses import dataclass, replace
import sys
sys.setrecursionlimit(100000)

@dataclass
class Block:
    idnum: int
    length: int
    pos: int
    processed: bool = False

def parse_input(fname):
    with open(fname) as f:
        line = f.read().strip()

    data_pos = []
    data_id = []
    gaps = []
    pos = 0
    for i, val in enumerate(line):
        ival = int(val)
        if i%2 == 0:
            data_pos += list(range(pos, pos+ival))
            data_id += [i//2]*ival
        else:
            gaps += list(range(pos, pos+ival))
        pos += ival

    return data_pos, data_id, gaps

data_pos, data_id, gaps = parse_input('9.input')
i = 0
while data_pos[-1 - i] > gaps[i]:
    old_pos = data_pos[-1 - i]
    data_pos[-1 - i] = gaps[i]
    gaps[i] = old_pos
    i += 1

score = 0
for pos, idnum in zip(data_pos, data_id):
    score += pos*idnum

print("Score: ", score)


#####Part 2#####

def parse_input_2(fname):
    with open(fname) as f:
        line = f.read().strip()

    blocks = []
    pos = 0
    for i, val in enumerate(line):
        ival = int(val)
        if i%2 == 0:
            blocks.append(Block(i//2, ival, pos))
        else:
            blocks.append(Block(-1, ival, pos))
        pos += ival

    return blocks

blocks = parse_input_2('9.input')

def compute_score(score, blocks):
    # print_blocks(blocks)
    # print(score)
    if len(blocks) == 0:
        return score
    new_block = blocks.pop()
    while new_block.idnum == -1:
        new_block = blocks.pop()
    found = False
    if not new_block.processed:
        for i, block in enumerate(blocks):
            if block.idnum == -1 and block.length >= new_block.length:
                if block.length > new_block.length:
                    blocks.insert(i+1, Block(-1, block.length - new_block.length, block.pos + new_block.length))

                block.idnum = new_block.idnum
                block.length = new_block.length
                block.processed = True

                found = True
                break
    if not found:
        score += sum(range(new_block.pos, new_block.pos+new_block.length))*new_block.idnum
    return compute_score(score, blocks)

        

print("Score 2 : ", compute_score(0, blocks))