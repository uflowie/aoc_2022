with open('input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

def get_start_marker(stream, num_distinct_chars):
	last_chars = stream[0:num_distinct_chars]
	for i in range(num_distinct_chars, len(stream)):
		if len(set(last_chars)) == num_distinct_chars:
			return i
		last_chars = last_chars[1:] + stream[i]

# part 1
print(get_start_marker(puzzle_input[0], 4))

# part 2
print(get_start_marker(puzzle_input[0], 14))