import re

with open('input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

def halve_string(s):
	half_length = len(s) // 2
	return s[:half_length], s[half_length:]

def mutual_item(first_half, second_half):
	for item in first_half:
		if item in second_half:
			return item

def get_priority(item):
	if re.match(r'^[a-z]+$', item) is not None:
		return ord(item) - ord('a') + 1
	else:
		return ord(item) - ord('A') + 27

# part 1
print(sum([get_priority(mutual_item(*halve_string(s))) for s in puzzle_input]))

def get_badge(first, second, third):
	for c in first:
		if c in second and c in third:
			return c

def get_groups(rucksacks):
	groups = []
	for i in range(0, len(rucksacks), 3):
		groups.append(rucksacks[i:i+3])
	return groups

# part 2
print(sum([get_priority(get_badge(*group)) for group in get_groups(puzzle_input)]))