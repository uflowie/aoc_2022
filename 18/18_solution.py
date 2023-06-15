import sys
sys.setrecursionlimit(2000)

with open('18/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

cubes = set()

for line in puzzle_input:
	x, y, z = map(int, line.split(','))
	cubes.add((x, y, z))

def get_non_diagonal_neighbors(cube):
	x, y, z = cube
	return [
		(x - 1, y, z),
		(x + 1, y, z),
		(x, y - 1, z),
		(x, y + 1, z),
		(x, y, z - 1),
		(x, y, z + 1),
	]

def get_uncovered_surfaces(cube, cubes):
	return len([n for n in get_non_diagonal_neighbors(cube) if n not in cubes])

# part 1
total_uncovered_surfaces = sum([get_uncovered_surfaces(cube, cubes) for cube in cubes])
print(total_uncovered_surfaces)

# part 2
def get_covered_surfaces(cube, cubes):
	return 6 - get_uncovered_surfaces(cube, cubes)

def find_outwards_surfaces(cubes):
	max_coordinate = max([max(cube) for cube in cubes]) + 1
	visited_cubes = set()
	amount_outwards_surfaces = 0
	next_cubes = set([(0, 0, 0)])
	while next_cubes:
		cube = next_cubes.pop()
		visited_cubes.add(cube)
		amount_outwards_surfaces += get_covered_surfaces(cube, cubes)
		neighbors = get_non_diagonal_neighbors(cube)
		neighbors = [neighbor for neighbor in neighbors if not (neighbor in visited_cubes or neighbor in cubes or any([c > max_coordinate for c in neighbor]) or any([c < 0 for c in neighbor]))]
		next_cubes.update(neighbors)
	return amount_outwards_surfaces


print(find_outwards_surfaces(cubes))
	