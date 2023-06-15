with open('20/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()

original_list = []
modified_list = []

for i in range(len(puzzle_input)):
	val = int(puzzle_input[i])
	if val == 0:
		zero = (val, i)
	x = (int(puzzle_input[i]), i)
	original_list.append(x)
	modified_list.append(x)

def move_and_insert(lst, x):
	val, _ = x
	
	if val == 0:
		return

	# Save the original index of x
	original_index = lst.index(x)

	# Remove x from the list
	lst.remove(x)

	# Calculate the new index for x by adding its value to the original index
	new_index = (original_index + val) % len(lst)

	# Insert x at the new index
	lst.insert(new_index, x)


for i in original_list:
	move_and_insert(modified_list, i)
	#print(f"moved {i}, new list: {modified_list}")

index = modified_list.index(zero)

# Define the target indices
indices = [1000, 2000, 3000]

# Use a list comprehension to find the elements at the target indices
elements = [modified_list[(index + i) % len(modified_list)] for i in indices]

print(elements)
# Find the sum of the elements
result = sum([val for val, _ in elements])

# Print the result
print(f"The result is {result}")

# part 2
original_list = [(val * 811589153, i) for (val, i) in original_list]
modified_list = original_list.copy()

# apply the move_and_insert function over the list 10 times
for i in range(10):
	print(f"iteration {i}")
	for x in original_list:
		move_and_insert(modified_list, x)

# Find the index of the element with value 0
index = modified_list.index(zero)

# find the sum as before
elements = [modified_list[(index + i) % len(modified_list)] for i in indices]
result = sum([val for val, _ in elements])

# Print the result
print(f"The result is {result}")
