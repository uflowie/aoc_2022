with open('input.txt', 'r') as input_file:
	puzzle_input = input_file.read().split("\n")[:-1]

"""
  X Y Z
A
B
C
"""
rock_paper_scissor_matrix = [
	[3, 6, 0],
	[0, 3, 6],
	[6, 0, 3]
]

symbol_mappings = {
	"X" : 0,
	"Y" : 1,
	"Z" : 2,
	"A" : 0,
	"B" : 1,
	"C" : 2
}

def get_moves(round_str):
	return [symbol_mappings[symbol] for symbol in round_str.split(" ")]

# part 1
def get_points_part_one(round_str):
	enemy_move, our_move = get_moves(round_str)
	return rock_paper_scissor_matrix[enemy_move][our_move] + (our_move + 1)

print(sum([get_points_part_one(round) for round in puzzle_input]))

# part 2
def get_points_part_two(round_str):
	enemy_move, our_move = get_moves(round_str)
	our_move = (our_move + enemy_move + 2) % 3
	return rock_paper_scissor_matrix[enemy_move][our_move] + (our_move + 1)

print(sum([get_points_part_two(round) for round in puzzle_input]))