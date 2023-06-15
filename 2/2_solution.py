with open('input.txt', 'r') as input_file:
	puzzle_input = input_file.read().split("\n")[:-1]

symbol_mappings = {
	"X" : 0,
	"Y" : 1,
	"Z" : 2,
	"A" : 0,
	"B" : 1,
	"C" : 2
}

scores_part_one = [3, 0, 6]

puzzle_input = [[symbol_mappings[symbol] for symbol in round_str.split(" ")] for round_str in puzzle_input]

def get_points(enemy_move, our_move):
	distance = (enemy_move - our_move) % 3
	# assuming the above mappings between letters A,B,C,X,Y,Z and 0..2 the modulo distance between
	# two letters identifies wins, losses and draws, as follows: 0 = draw, 1 = loss, 2 = win
	return scores_part_one[distance] + (our_move + 1) # the points for picking X,Y,Z are included in the mapping if we add one to it

# part 1
print(sum([get_points(enemy_move, our_move) for enemy_move, our_move in puzzle_input]))

# part 2 - since the distance between two letters can tell us whether a round was won, we can also
# infer that given the enemy move, we can calculate the distance needed to provoke a win/loss/draw
# we need to mildly modify the mapping so that we can simply add our move to the enemy move to get
# the desired result
print(sum([get_points(enemy_move, (enemy_move + our_move + 2) % 3) for enemy_move, our_move in puzzle_input]))
