import json

with open('13/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

def parse_packet(line):
	return json.loads(line)

def pair_in_order(left, right):
	left_type = type(left)
	right_type = type(right)
	if left_type == int and right_type == int:
		return left - right
	elif left_type == list and right_type == list:
		for i in range(len(left)):
			if i > len(right) - 1:
				# right ran out of elements - incorrectly ordered
				return 1
			compared = pair_in_order(left[i], right[i])
			if compared != 0:
				return compared
		# left ran out of elements - correctly ordered if right still has elements
		return len(left) - len(right)
	elif left_type == list:
		return pair_in_order(left, [right])
	elif right_type == list:
		return pair_in_order([left], right)


# part 1
pairs = [[parse_packet(puzzle_input[i]), parse_packet(puzzle_input[i + 1])] for i in range(0, len(puzzle_input), 3)]
pairs = [pair_in_order(left, right) for left, right in pairs]
in_order_indices = [i + 1 for i, x in enumerate(pairs) if x < 0]
print(f"sum of ordered indices: {sum(in_order_indices)}")

# part 2
pairs = [parse_packet(line) for line in puzzle_input if line != ""]
marker_1 = [[2]]
marker_2 = [[[6]]]
pairs.extend([marker_1, marker_2])

for i in range(len(pairs)):
	for j in range(i + 1, len(pairs)):
		if pair_in_order(pairs[i], pairs[j]) > 0:
			pairs[i], pairs[j] = pairs[j], pairs[i]

print(f"multiplied indices of markers: {(pairs.index(marker_1) + 1) * (pairs.index(marker_2) + 1)}")