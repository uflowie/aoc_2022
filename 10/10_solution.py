# yes, really

operations_per_cycle = [item for sublist in map(lambda line: [0] if line.split()[0]== "noop" else [0, int(line.split()[1])], open('10/input.txt', 'r').read().splitlines()) for item in sublist]
register_values = [sum(operations_per_cycle[0:i]) + 1 for i in range(0, len(operations_per_cycle))]

print(sum(register_values[i] * (i + 1) for i in range(19, 259, 40)), "\n".join(["".join(a) for a in [["#" if abs(register_value - i) <= 1 else "." for i, register_value in enumerate(a)] for a in [register_values[i:i + 40] for i in range(0, len(register_values), 40)]]]), sep="\n")
