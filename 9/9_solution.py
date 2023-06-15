with open('9/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

# get sign of an int
def sign_or_zero(x):
	return 0 if x == 0 else(1, -1)[x < 0]

# add two tuples together
def add_tuples(a, b):
	return tuple(map(sum, zip(a, b)))

def subtract_tuples(a, b):
	return tuple(map(lambda x, y: x - y, a, b))

movements = {
	'U': (0, 1),
	'D': (0, -1),
	'R': (1, 0),
	'L': (-1, 0)
}

def get_tail_movement(head, tail):
	direction = subtract_tuples(head, tail)
	return [sign_or_zero(a) if any(abs(b) > 1 for b in direction) else 0 for a in (direction)]

def update_knots(knots, movement):
	knots[0] = add_tuples(knots[0], movement)
	for i in range(0, len(knots) - 1):
		knots[i + 1] = add_tuples(knots[i + 1], get_tail_movement(knots[i], knots[i + 1]))
		if i == len(knots) - 2:
			return knots[i + 1]

def move_rope_around(knots):
	tail_positions = set()
	for line in puzzle_input:
		movement, count = movements[line[0]], int(line[2:])
		for _ in range(count):
			tail = update_knots(knots, movement)
			tail_positions.add(tail)
	return len(tail_positions)


# part 1
print(move_rope_around([(0, 0) for _ in range(2)]))

# part 2
print(move_rope_around([(0, 0) for _ in range(10)]))
