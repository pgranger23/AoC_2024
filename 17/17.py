import re

def parse_input(fname):
    with open(fname) as f:
        lines = f.readlines()
    
    registers = [0, 0, 0]
    for i in range(3):
        registers[i] = int(re.findall(r'\d+', lines[i])[0])

    instructions = list(map(int, re.findall(r'\d+', lines[4])))

    return registers, instructions

class Program:
    def __init__(self, registers, instructions):
        self.registers = registers
        self.instructions = instructions
        self.pointer = 0
        self.output = []

        self.operation_map = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv
        }

    def run(self):
        while self.pointer < len(self.instructions):
            operation = self.instructions[self.pointer]
            value = self.instructions[self.pointer + 1]
            self.operation_map[operation](value)

    def get_combo(self, value):
        if value <= 3:
            return value
        if value == 4:
            return self.registers[0]
        if value == 5:
            return self.registers[1]
        if value == 6:
            return self.registers[2]
        if value == 7:
            raise ValueError('Invalid value')

    def adv(self, value):
        numerator = self.registers[0]
        denominator = 2**self.get_combo(value)
        result =  int(numerator / denominator)
        self.registers[0] = result
        self.pointer += 2
    
    def bxl(self, value):
        self.registers[1] = self.registers[1] ^ value
        self.pointer += 2
    
    def bst(self, value):
        self.registers[1] = self.get_combo(value)%8
        self.pointer += 2
    
    def jnz(self, value):
        if self.registers[0] == 0:
            self.pointer += 2
        else:
            self.pointer = value
    
    def bxc(self, value):
        self.registers[1] = self.registers[1] ^ self.registers[2]
        self.pointer += 2

    def out(self, value):
        self.output.append(self.get_combo(value)%8)
        self.pointer += 2

    def bdv(self, value):
        numerator = self.registers[0]
        denominator = 2**self.get_combo(value)
        result =  int(numerator / denominator)
        self.registers[1] = result
        self.pointer += 2
    
    def cdv(self, value):
        numerator = self.registers[0]
        denominator = 2**self.get_combo(value)
        result =  int(numerator / denominator)
        self.registers[2] = result
        self.pointer += 2

    def get_joined_output(self):
        return ','.join(map(str, self.output))

registers, instructions = parse_input('17.input')

program = Program(registers, instructions)
program.run()

print(program.get_joined_output())


####Part 2####

#Trying to reconstruct input in base 8

matching = [[]]
full_matches = []

while matching:
    cur_seq = matching.pop()
    nb_digit_seq = len(cur_seq)
    cur_nb = sum([d*(8**(len(instructions) - 1 - i)) for i, d in enumerate(cur_seq)])

    next_digit_to_match = instructions[-1 - nb_digit_seq]
    for possible_bit in range(8):
        new_nb = cur_nb + possible_bit*(8**(len(instructions) - 1 - nb_digit_seq))
        registers[0] = new_nb
        program = Program(registers, instructions)
        program.run()
        # print(program.output)
        if(len(program.output) < nb_digit_seq + 1):
            continue
        if program.output[-1 - nb_digit_seq] == next_digit_to_match:
            new_seq = cur_seq.copy()
            new_seq.append(possible_bit)
            
            if len(new_seq) == len(instructions):
                print(f"Found sequence {new_seq} with value {new_nb}")
                full_matches.append(new_nb)
                continue
            matching.append(new_seq)

print("Smallest value is", min(full_matches))


