with open('17/input.txt', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()

def piece_collides(piece, resting_pieces):
    for (x, y) in piece:
        if (x, y) in resting_pieces:
            return True
    return any([x > 6 for (x, _) in piece]) or any([x < 0 for (x, _) in piece]) or any([y < 1 for (_, y) in piece])

def normalize_resting_pieces(resting_pieces):
	# normalize resting pieces
	min_x = min([x for (x, _) in resting_pieces])
	min_y = min([y for (_, y) in resting_pieces])
	resting_pieces = [(x - min_x, y - min_y) for (x, y) in resting_pieces]
	return resting_pieces

def hash_resting_pieces(resting_pieces):
	resting_pieces = normalize_resting_pieces(resting_pieces)
	resting_pieces = sorted(resting_pieces)
	return ''.join([str(x) + ',' + str(y) + ';' for (x, y) in resting_pieces])

pieces = [
		[(2, 4), (3, 4), (4, 4), (5, 4)],  			# horizontal line
		[(3, 4), (2, 5), (3, 5), (4, 5), (3, 6)], 	# cross
		[(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)],  	# flipped L
		[(2, 4), (2, 5), (2, 6), (2, 7)],  			# vertical line
		[(2, 4), (2, 5), (3, 4), (3, 5)]  			# square
		
]

def simulate_rocks(max_rocks):
	i = 1
	piece = pieces[0]
	resting_pieces = []
	previous_max = 0
	improvements = []
	potential_cycle_entries = {}

	while i <= max_rocks:
	# check if the highest pieces form a line
		for j in range(len(puzzle_input[0])):
			char = puzzle_input[0][j]
			if i > max_rocks:
				break
			# apply jet
			if char == '<':
				new_pos = [(x - 1, y) for (x, y) in piece]
			elif char == '>':
				new_pos = [(x + 1, y) for (x, y) in piece]
			if not piece_collides(new_pos, resting_pieces):
				piece = new_pos
			# move down
			new_pos = [(x, y - 1) for (x, y) in piece]
			if piece_collides(new_pos, resting_pieces):
				resting_pieces += piece
				max_height = max(previous_max, max([y for (_, y) in piece]))
				improvements.append(max_height - previous_max)
				previous_max = max_height
				for (_, y) in piece:
					line_found = False
					for h in range(0, 7):
						if (h, y) not in resting_pieces:
							break
						if h == 6:
							line_found = True
					if line_found:
						resting_pieces = [p for p in resting_pieces if p[1] >= y]
						potential_cycle_entry = (j, hash_resting_pieces(resting_pieces), i % 5)
						if potential_cycle_entry in potential_cycle_entries:
							height, rocks = potential_cycle_entries[potential_cycle_entry]
							cycle_height = max_height - height
							rock_count = i - rocks
							cycle_iterations = (max_rocks - i) // rock_count
							height_gained_in_iterations = cycle_height * cycle_iterations
							remaining_rocks = (max_rocks - i) % rock_count
							remaining_height = sum(improvements[rocks:rocks + remaining_rocks])
							final_height = max_height + height_gained_in_iterations + remaining_height
							return final_height
						potential_cycle_entries[potential_cycle_entry] = (max_height, i)
						break
				piece = pieces[i % 5]
				piece = [(x, y + max_height) for (x, y) in piece]
				i += 1
			else:
				piece = new_pos
	return previous_max


# print highest piece
print(simulate_rocks(1000000000000))
print(simulate_rocks(2022))