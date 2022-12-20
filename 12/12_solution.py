with open('12/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

def get_height_ord(height):
	if height == "S":
		return ord("a")
	if height == "E":
		return ord("z")
	return ord(height)

def get_reachable_neighbors(node, heightmap):
	x, y, height = node
	neighbors = []
	if x > 0:
		neighbors.append((x - 1, y, heightmap[y][x - 1]))
	if x < len(heightmap[0]) - 1:
		neighbors.append((x + 1, y, heightmap[y][x + 1]))
	if y > 0:
		neighbors.append((x, y - 1, heightmap[y - 1][x]))
	if y < len(heightmap) - 1:
		neighbors.append((x, y + 1, heightmap[y + 1][x]))
	return filter(lambda n: get_height_ord(n[2]) <= get_height_ord(height) + 1, neighbors)

def get_heightmap(puzzle_input):
	heightmap = []
	for y, line in enumerate(puzzle_input):
		heightmap.append([])
		for x, char in enumerate(line):
			heightmap[y].append(char)
	return heightmap

def get_character(heightmap, character):
	for y, line in enumerate(heightmap):
		for x, char in enumerate(line):
			if char == character:
				return (x, y, character)

def get_shortest_path_length(start, end, heightmap):
	# get the shortest path from start to end and print its length
	next_batch = [start]
	visited = set()
	i = 0
	while end not in next_batch and next_batch:
		i += 1
		current_batch = next_batch
		next_batch = []
		for node in current_batch:
			for neighbor in get_reachable_neighbors(node, heightmap):
				if neighbor not in visited:
					next_batch.append(neighbor)
					visited.add(neighbor)
	return i if end in next_batch else 2**32


# part 1
heightmap = get_heightmap(puzzle_input)
start = get_character(heightmap, "S")
end = get_character(heightmap, "E")
print(f"shortest path from S {get_shortest_path_length(start, end, heightmap)}")

# part 2
# find all "a" in the heightmap and their shortest path to the end
# then print the length of the shortest path
a_nodes = []
for y, line in enumerate(heightmap):
	for x, char in enumerate(line):
		if char == "a":
			a_nodes.append((x, y, char))
print(min(map(lambda a: get_shortest_path_length(a, end, heightmap), a_nodes)))
