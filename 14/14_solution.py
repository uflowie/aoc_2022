with open('14/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

def get_rocks():
	rocks = set()
	for line in puzzle_input:
		coords = line.split(' -> ')
		for i in range(len(coords) - 1):
			from_x, from_y = [int(c) for c in coords[i].split(',')]
			to_x, to_y = [int(c) for c in coords[i + 1].split(',')]
			# add all points on the line between the two points
			for x in range(from_x, to_x + sign(to_x - from_x), sign(to_x - from_x)):
				for y in range(from_y, to_y + sign(to_y - from_y), sign(to_y - from_y)):
					rocks.add((x, y))
	return rocks


def sign(x):
	return 1 if x >= 0 else -1

# part 1
def simulate_sands_falling_part_1():
	rocks = get_rocks()
	sands = 0
	sand = (500, 0)
	while sand[1] <= max([r[1] for r in rocks]):
		if (sand[0], sand[1] + 1) not in rocks:
			sand = (sand[0], sand[1] + 1)
		elif (sand[0] - 1, sand[1] + 1) not in rocks:
			sand = (sand[0] - 1, sand[1] + 1)
		elif (sand[0] + 1, sand[1] + 1) not in rocks:
			sand = (sand[0] + 1, sand[1] + 1)
		else:
			sands += 1
			rocks.add(sand)
			sand = (500, 0)
	return sands

print(f"number of sands that fell before tumbling into the infinite abyss: {simulate_sands_falling_part_1()}")

# part 2
def simulate_sands_falling_part_2():
	rocks = get_rocks()
	max_depth = max([r[1] for r in rocks]) + 2
	sands = 0
	sand = (500, 0)
	while (500, 0) not in rocks:
		sand_moved = True
		if (sand[1] + 1) == max_depth:
			sand_moved = False
		elif (sand[0], sand[1] + 1) not in rocks:
			sand = (sand[0], sand[1] + 1)
		elif (sand[0] - 1, sand[1] + 1) not in rocks:
			sand = (sand[0] - 1, sand[1] + 1)
		elif (sand[0] + 1, sand[1] + 1) not in rocks:
			sand = (sand[0] + 1, sand[1] + 1)
		else:
			sand_moved = False
		if not sand_moved:
			sands += 1
			rocks.add(sand)
			sand = (500, 0)
	return sands
	
print(f"number of sands that fell before blocking the entrance: {simulate_sands_falling_part_2()}")

