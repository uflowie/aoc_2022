with open('input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

def parse_stacks_and_movements(puzzle_input):
	for i in range(0, len(puzzle_input)):
		if puzzle_input[i] == "":
			original_configuration = puzzle_input[0:i - 1] # we are not interested in the crate stack numbers line
			crate_movements = puzzle_input[i + 1:]
	stack_numbers = (len(original_configuration[0]) + 1) // 4
	stacks = [[] for _ in range(stack_numbers)]
	for line in original_configuration[-1::-1]:
		for stack_number in range(stack_numbers):
			stack_string_index = 1 + stack_number * 4
			crate = line[stack_string_index]
			if crate != " ":
				stacks[stack_number].append(crate)	
	return stacks, crate_movements

# parse a string like "move <x> from <stack a> to <stack b>""
def parse_crate_movement(crate_movement):
	words = crate_movement.split(" ")
	num_crates = int(words[1])
	from_stack = int(words[3]) - 1
	to_stack = int(words[5]) - 1
	return num_crates, from_stack, to_stack

def top_crates(stacks):
	return "".join([stack[-1] if len(stack) > 0 else "" for stack in stacks])

def solve_crates(crate_movement_function):
	stacks, crate_movements = parse_stacks_and_movements(puzzle_input)
	for crate_movement in crate_movements:
		num_crates, from_stack, to_stack = parse_crate_movement(crate_movement)
		crate_movement_function(stacks, num_crates, from_stack, to_stack)
	print(top_crates(stacks))

# part 1
def move_crate_part_one(stacks, num_crates, from_stack, to_stack):
	for _ in range(num_crates):
		crate = stacks[from_stack].pop()
		stacks[to_stack].append(crate)

solve_crates(move_crate_part_one)

# part 2
def move_crate_part_two(stacks, num_crates, from_stack, to_stack):
	temporary_stack = []
	for _ in range(num_crates):
		crate = stacks[from_stack].pop()
		temporary_stack.append(crate)
	for _ in range(num_crates):
		crate = temporary_stack.pop()
		stacks[to_stack].append(crate)

solve_crates(move_crate_part_two)
