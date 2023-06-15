import re

with open('15/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

# calculate the manhattan distance between two points
def manhattan_distance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# part 1
def get_beaconless_points_on_line(sensor, beacon, line_y):
	# make a square around the sensor and beacon to approximate a circle within which no other beacons can be
	distance = manhattan_distance(sensor, beacon)
	print(distance)
	square_x = sensor[0] - distance
	square_side_length = 2 * distance

	# find all points on the line that are closer or equal distance to the sensor as the beacon
	line_x = square_x
	line_side_length = square_side_length
	points_on_line =  [(line_x + i, line_y) for i in range(line_side_length)]
	return [point for point in points_on_line if manhattan_distance(sensor, point) <= distance]

def get_beaconless_points_on_line_with_ranges(sensors, beacons, line_y, max_range):
	intersection_ranges = []
	for sensor, beacon in zip(sensors, beacons):
		intersection_range = get_intersection_range(sensor, beacon, line_y, max_range)
		if intersection_range is not None:
			intersection_ranges.append(intersection_range)
	# merge intersection ranges
	intersection_ranges.sort(key=lambda x: x[0])
	curr = intersection_ranges[0]
	for intersection_range in intersection_ranges[1:]:
		if curr[1] + 1 < intersection_range[0]:
			return {curr[1] + 1, line_y}
		else:
			curr = (curr[0], max(curr[1], intersection_range[1]))
	return None
			

def get_intersection_range(sensor, beacon, line_y, max_range):
	distance = manhattan_distance(sensor, beacon)
	if abs(sensor[1] - line_y) > distance:
		return None
	else:
		return (max(0, sensor[0] - distance + abs(sensor[1] - line_y)), min(max_range, sensor[0] + distance - abs(sensor[1] - line_y)))

beaconless_points = set()
beacons = set()

for line in puzzle_input:
	sensor, beacon = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
	sensor, beacon = (int(sensor[0]), int(sensor[1])), (int(beacon[0]), int(beacon[1]))
	#beaconless_points.update(get_beaconless_points_on_line(sensor, beacon, 2000000))
	beacons.add(beacon)

# remove beacons form beaconless points
beaconless_points.difference_update(beacons)
print(len([point for point in beaconless_points if point[1] == 2000000]))

# part 2
sensors = []
beacons = []

for line in puzzle_input:
	sensor, beacon = re.findall(r'x=(-?\d+), y=(-?\d+)', line)
	sensor, beacon = (int(sensor[0]), int(sensor[1])), (int(beacon[0]), int(beacon[1]))
	sensors.append(sensor)
	beacons.append(beacon)

max_range = 4000000

get_intersection_range((8, 7), (2, 10), 7, max_range)
for line_y in range(max_range):
	if line_y % 1000 == 0:
		print(line_y)
	res = get_beaconless_points_on_line_with_ranges(sensors, beacons, line_y, max_range)
	if res is not None:
		x, y = res
		print(f"found beacon at x={x}, y={y}")
		print(f"tuning frequency: {x * max_range + y}")
		break