with open('input.txt') as input_file:
	puzzle_input = input_file.read()

# part 1 - some list comprehension practice
total_calories_per_elf = [sum([int(calories) for calories in elf_calories_as_string_lists]) for elf_calories_as_string_lists in [elf_as_string.splitlines() for elf_as_string in puzzle_input.split("\n\n")]]
print("part 1 solution - maximum calories carried by one elf is:")
print(max(total_calories_per_elf))

# part 2
print("part 2 solution - maximum calories carried by the top three elves is:")
total_calories_per_elf.sort(reverse=True)
print(sum(total_calories_per_elf[0:3]))