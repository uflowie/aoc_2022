with open('16/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

valves = []
valves_with_non_zero_flow = set()
valve_neighbors = {}

distances = {}

def minutes_to_valve(from_valve, to_valve):
	if (from_valve, to_valve) in distances:
		return distances[(from_valve, to_valve)]
	else:
		distances_from_start = {}
		for valve in valves:
			distances_from_start[valve] = 2**32
		distances_from_start[from_valve] = 0
		unvisited_nodes = valves.copy()
		while len(unvisited_nodes) > 0:
			smallest_distance = 2**32
			for valve in unvisited_nodes:
				if distances_from_start[valve] < smallest_distance:
					smallest_distance = distances_from_start[valve]
					current_node = valve
			unvisited_nodes.remove(current_node)
			for neighbor in valve_neighbors[current_node]:
				if neighbor in unvisited_nodes:
					alternative_distance = distances_from_start[current_node] + 1
					if alternative_distance < distances_from_start[neighbor]:
						distances_from_start[neighbor] = alternative_distance
		distance_from_start_to_end = distances_from_start[to_valve] + 1
		distances[(from_valve, to_valve)] = distance_from_start_to_end
		distances[(to_valve, from_valve)] = distance_from_start_to_end
		return distance_from_start_to_end


for line in puzzle_input:
	# parse the valve name and neighbor names from a string like "Valve PL has flow rate=4; tunnels lead to valves LI, GD, LB, IA, LZ"
	valve_name = line.split(" ")[1]
	# parse the flow rate from a string like "Valve RM has flow rate=17;"
	flow_rate = int(line.split("flow rate=")[1].split(";")[0])
	# parse the neighbor names from a string like "tunnels lead to valves LI, GD, LB, IA, LZ" or "tunnel leads to valve KU"
	line = "".join(line.split("; ")[1])
	neighbor_names = line.split("tunnels lead to valves ")[1].split(", ") if "tunnels lead to valves " in line else line.split("tunnel leads to valve ")[1].split(", ")
	valves.append(valve_name)
	valve_neighbors[valve_name] = neighbor_names
	if flow_rate > 0:
		valves_with_non_zero_flow.add((valve_name, flow_rate))

def simulate(turned_on, minutes, current_node, released, flows):
	reachable = [valve for valve in (valves_with_non_zero_flow - turned_on) if minutes_to_valve(current_node[0], valve[0]) <= 30 - minutes]
	if len(reachable) == 0:
		flows.append((released + sum([flow for _, flow in turned_on]) * (30 - minutes), turned_on))
	else:
		for valve_to_turn_on in reachable:
			new_turned_on = turned_on.copy()
			new_turned_on.add(valve_to_turn_on)
			distance_to_valve = minutes_to_valve(current_node[0], valve_to_turn_on[0])
			simulate(new_turned_on, minutes + distance_to_valve, valve_to_turn_on, released + sum([flow for _, flow in turned_on]) * distance_to_valve, flows)
	return flows

# part 1

flows = simulate(set(), 0, ('AA', 0), 0, [])
print(max(flows))

# part 2
# get all disjoint pairs of turned_on valves in flows
flows = simulate(set(), 4, ('AA', 0), 0, [])
flows.sort(key=lambda x: x[0], reverse=True)
best_disjoint = 0

for i in range(len(flows)):
	if i % 10000 == 0:
		print(i)
	for j in range(i + 1, len(flows)):
			if flows[i][0] + flows[j][0] < best_disjoint:
				break
			if flows[i][1].isdisjoint(flows[j][1]):
				disjoint_released = flows[i][0] + flows[j][0]
				if disjoint_released > best_disjoint:
					best_disjoint = disjoint_released
					break

print(best_disjoint)

