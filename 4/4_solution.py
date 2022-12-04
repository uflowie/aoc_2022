with open('input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

def get_ranges(assignments):
	ranges = assignments.split(",")
	return [range(int(r.split('-')[0]), int(r.split('-')[1]) + 1) for r in ranges]

def range_fully_contained(range_a, range_b):
	return (range_a.start <= range_b.start and range_a.stop >= range_b.stop) or (range_a.start >= range_b.start and range_a.stop <= range_b.stop)

# get ranges in the form [[range(a, b), range(c, d)], ...]
all_ranges = [get_ranges(a) for a in puzzle_input]

# part 1
print(sum([range_fully_contained(*r) for r in all_ranges]))

# part 2
def ranges_overlap(ranges):
	# if the range with the smaller start ends before the other one begins, they don't overlap
	ranges.sort(key=lambda r: r.start)
	return not ranges[0].stop <= ranges[1].start

print(sum([ranges_overlap(r) for r in all_ranges]))