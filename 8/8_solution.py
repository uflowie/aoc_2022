from functools import reduce

with open('8/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()
		
def get_tree_metrics(x, y, height, trees):
	left_trees = list(reversed(trees[x][0:y]))
	right_trees = trees[x][y + 1:]
	up_trees = list(reversed([line[y] for line in trees[0:x]]))
	down_trees = [line[y] for line in trees[x + 1:]]
	adjacent_trees = [left_trees, right_trees, up_trees, down_trees]
	visible = any(max(trees, default=-1) < height for trees in adjacent_trees)
	# find the first index of a tree that is higher than this tree, lenght of adjacent trees if there is none
	scenic = lambda adjacent: next((i + 1 for i, tree in enumerate(adjacent) if tree >= height), len(adjacent))
	product = lambda l: reduce(lambda x, y: x * y, l)
	scenic_score = product(map(scenic, adjacent_trees))
	return (visible, scenic_score)

# map a two dimensional array of trees to a two dimension array of tree metrics
def get_tree_metrics_map(trees):
	mapped_trees = [line[:] for line in trees]
	for x, line in enumerate(trees):
		for y, height in enumerate(line):
			mapped_trees[x][y] = get_tree_metrics(x, y, height, trees)
	return mapped_trees

puzzle_input = [[int(character) for character in list(line)] for line in puzzle_input]
tree_metrics = get_tree_metrics_map(puzzle_input)

# part 1
visible_trees = sum(1 for line in tree_metrics for tree in line if tree[0])
print(visible_trees)

# part 2
scenic_score = max(tree[1] for line in tree_metrics for tree in line)
print(scenic_score)