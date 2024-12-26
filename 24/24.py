from dataclasses import dataclass

@dataclass
class Node:
    label: str
    value: int
    input: "Operation"
    outputs: list["Operation"]

    def __hash__(self):
        return hash(self.label)
    
    def __repr__(self):
        return f"{self.label}: {self.value}"

@dataclass
class Operation:
    op: str
    left: Node
    right: Node
    out: Node
    processed: bool = False

    def process(self):
        if self.processed:
            return False
        if self.left.value is None or self.right.value is None:
            return False
        if self.op == 'AND':
            self.out.value = self.left.value & self.right.value
        elif self.op == 'OR':
            self.out.value = self.left.value | self.right.value
        elif self.op == 'XOR':
            self.out.value = self.left.value ^ self.right.value
        self.processed = True
        return True

    def __hash__(self):
        return hash((self.op, self.left, self.right, self.out))
    
    def __repr__(self):
        return f"{self.left} {self.op} {self.right} -> {self.out}"

def parse_input(fname):
    with open(fname) as f:
        lines = f.read().splitlines()
    
    sep = lines.index('')
    values = [x.split(': ') for x in lines[:sep]]
    operations = [x.split() for x in lines[sep+1:]]
    
    values = {k: int(v) for k, v in values}
    operations = [(a, b, c, e) for a, b, c, d, e in operations]

    return values, operations

values_inp, operations_inp = parse_input("24.input")

def simulate(operations_inp, values_inp):
    nodes = {k: Node(k, v, None, []) for k, v in values_inp.items()}
    for _, _, _, node in operations_inp:
        if not node in nodes:
            nodes[node] = Node(node, None, None, [])

    operations = [Operation(b, nodes[a], nodes[c], nodes[e]) for a, b, c, e in operations_inp]

    for operation in operations:
        operation.left.outputs.append(operation)
        operation.right.outputs.append(operation)
        operation.out.input = operation

        to_process = set(operations)

        while to_process:
            current = to_process.pop()
            if current.process():
                to_process.update(current.out.outputs)
    return nodes

sim_nodes = simulate(operations_inp, values_inp)

z_nodes = sorted([x for x in sim_nodes.values() if x.label[0] == 'z'], key=lambda x: x.label, reverse=True)
bits = 0
for node in z_nodes:
    bits = (bits << 1) | node.value

x_nodes = sorted([x for x in sim_nodes.values() if x.label[0] == 'x'], key=lambda x: x.label, reverse=True)
y_nodes = sorted([x for x in sim_nodes.values() if x.label[0] == 'y'], key=lambda x: x.label, reverse=True)

x_bits = 0
for node in x_nodes:
    x_bits = (x_bits << 1) | node.value
y_bits = 0
for node in y_nodes:
    y_bits = (y_bits << 1) | node.value

print("Part 1:", bits)
print("Part 2:", "dck,fgn,nvh,qdg,vvf,z12,z19,z37") #Hand calculated... I'm not going to write a solver for this. It's not worth it.