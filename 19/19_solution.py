import re

with open('19/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()


def add_tuple(t1, t2):
	return tuple([t1[i] + t2[i] for i in range(len(t1))])

def subtract_tuple(t1, t2):
	return tuple([t1[i] - t2[i] for i in range(len(t1))])

def construction_affordable(resources, cost):
	return all([x >= 0 for x in subtract_tuple(resources, cost)])

def filter_suboptimal_states(states, minutes, blueprint, max_minutes):
	new_states = states.copy()
	best_geodes_state = max(states, key=lambda x: x[0][3])

	best_geodes = best_geodes_state[0][3]
	best_geode_bots = best_geodes_state[1][3]
	min_best_potential_geodes = best_geodes + (max_minutes - minutes) * best_geode_bots
	best_resources, best_bots = best_geodes_state

	max_ore_cost = max([blueprint[i][0] for i in range(4)])
	max_clay_cost = max([blueprint[i][1] for i in range(4)])
	max_obsidian_cost = max([blueprint[i][2] for i in range(4)])
	if best_geodes == 0:
		return states
	for state in states:
		if state == best_geodes_state:
			continue
		resources, bots = state
		ore_bots, clay_bots, obsidian_bots, geode_bots = bots
		max_potential_geodes = resources[3] + (max_minutes - minutes) * geode_bots + sum(range(max_minutes - minutes + 1))
		if max_ore_cost < ore_bots or max_clay_cost < clay_bots or max_obsidian_cost < obsidian_bots or max_potential_geodes < min_best_potential_geodes:
			new_states.remove(state)
		elif all([resources[i] <= best_resources[i] for i in range(4)]) and all([bots[i] <= best_bots[i] for i in range(4)]):
			new_states.remove(state)
	return new_states

# ore, clay, obsidian, geode
def get_new_states(state, blueprint):
	resources, bots = state
	new_resources = add_tuple(resources, bots)
	new_states = []
	new_states.append((new_resources, bots)) # do nothing
	for i in range(4):
		if construction_affordable(resources, blueprint[i]):
			resources_minus_cost = subtract_tuple(new_resources, blueprint[i])
			new_bots = add_tuple(tuple([1 if i == j else 0 for j in range(4)]), bots)
			new_states.append((resources_minus_cost, new_bots))
	return new_states
	

def parse_blueprint(line):
	blueprint = []
	for part in line.split('. '):
		ore, clay, obsidian, geode = 0, 0, 0, 0
		for match in re.findall(r'(\d+) ore', part):
			ore += int(match)
		for match in re.findall(r'(\d+) clay', part):
			clay += int(match)
		for match in re.findall(r'(\d+) obsidian', part):
			obsidian += int(match)
		for match in re.findall(r'(\d+) geode', part):
			geode += int(match)
		blueprint.append((ore, clay, obsidian, geode))
	return tuple(blueprint)


def max_geode_for_blueprint(blueprint, max_minutes):
	initial_state = ((0, 0, 0, 0), (1, 0, 0, 0))
	current_states = set([initial_state])
	minutes = 0
	while minutes < 32:
		print(minutes)
		print(len(current_states))
		new_states = set()
		for state in current_states:
			new_states.update(get_new_states(state, blueprint))
		current_states = filter_suboptimal_states(new_states, minutes, blueprint, max_minutes)
		minutes += 1
	return max([geode for ((_, _, _, geode), _) in current_states])


sum_quality_levels = 0

"""for i in range(len(puzzle_input)):
	line = puzzle_input[i]
	blueprint = parse_blueprint(line)
	max_geodes = max_geode_for_blueprint(blueprint, 32)
	quality_level = (i + 1) * max_geodes
	sum_quality_levels += quality_level

print(f"sum of quality levels: {sum_quality_levels}")"""


maxes_geodes_multiplied = 1

# part 2
for i in range(3):
	line = puzzle_input[i]
	blueprint = parse_blueprint(line)
	max_geodes = max_geode_for_blueprint(blueprint, 32)
	maxes_geodes_multiplied *= max_geodes

print(f"max geodes multiplied: {maxes_geodes_multiplied}")