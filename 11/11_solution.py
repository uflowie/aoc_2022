with open('11/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().split("\n\n")

class Monkey:
	def __init__(self, items, operation, divisible_by, true_destination, false_destination):
		self.items = items
		self.operation = operation
		self.divisible_by = divisible_by
		self.total_inspections = 0
		self.true_destination = true_destination
		self.false_destination = false_destination

	def take_turn(self, all_monkeys, relief_function):
		for item in self.items:
			item.apply_operation(self.operation)
			relief_function(item)
			destination = all_monkeys[self.true_destination if item.divisible_by(self.divisible_by) else self.false_destination]
			destination.items.append(item)
			self.total_inspections += 1
		self.items = []

def get_operation(operation_string):
	parts = operation_string.split()
	if parts[1] == "*":
		return lambda item: item * item if parts[2] == "old" else item * int(parts[2])
	elif parts[1] == "+":
		return lambda item: item + int(parts[2])

def parse_monkey(monkey_string):
	monkey_string_lines = monkey_string.splitlines()
	divisible_by = int(monkey_string_lines[3].split("Test: divisible by ")[1])
	items = [int(item) for item in monkey_string_lines[1].split("Starting items: ")[1].split(", ")]
	operation = get_operation(monkey_string_lines[2].split("Operation: new = ")[1])
	true_destination = int(monkey_string_lines[4].split("If true: throw to monkey ")[1])
	false_destination = int(monkey_string_lines[5].split("If false: throw to monkey ")[1])
	return Monkey(items, operation, divisible_by, true_destination, false_destination)

def monkey_around(turns, relief_function):
	monkeys = [parse_monkey(monkey_string) for monkey_string in puzzle_input]
	monkey_modulos = [monkey.divisible_by for monkey in monkeys]
	for monkey in monkeys:
		monkey.items = [Item(item, monkey_modulos) for item in monkey.items]
	for _ in range(turns):
		for monkey in monkeys:
			monkey.take_turn(monkeys, relief_function)
	inspection_1, inspection_2 = [monkey.total_inspections for monkey in sorted(monkeys, key=lambda monkey: monkey.total_inspections, reverse=True)[:2]]
	print(inspection_1 * inspection_2)

class Item:
	def __init__(self, value, monkey_modulos):
		self.monkey_modulos = monkey_modulos
		self.representations = [value] * len(monkey_modulos)

	def apply_operation(self, operation):
		self.representations = [operation(representation) for representation in self.representations]

	def compress(self):
		self.representations = [representation % modulo for representation, modulo in zip(self.representations, self.monkey_modulos)]

	def divisible_by(self, divisor):
		return self.representations[self.monkey_modulos.index(divisor)] % divisor == 0

# part 1
monkey_around(20, lambda item: item.apply_operation(lambda val: val // 3))

# part 2
monkey_around(10000, lambda item: item.compress())

