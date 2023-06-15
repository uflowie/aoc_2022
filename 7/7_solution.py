with open('7/input.txt', 'r') as input_file:
	puzzle_input = input_file.read().splitlines()[1:] # skip root directory

class Directory:
	def __init__(self, name):
		self.name = name
		self.dirs = {}
		self.files = {}

	def add_file(self, file_name, file_size):
		if file_name not in self.files:
			self.files[file_name] = File(file_name, file_size)

	def add_dir(self, dir_name):
		if dir_name not in self.dirs:
			self.dirs[dir_name] = Directory(dir_name)
		
	def get_size(self):
		return sum([file.size for file in self.files.values()]) + sum([dir.get_size() for dir in self.dirs.values()])

	def get_subdirs(self):
		return list(self.dirs.values()) + [subdir for dir in self.dirs.values() for subdir in dir.get_subdirs()]

class File:
	def __init__(self, name, size):
		self.name = name
		self.size = size


def make_file_system(puzzle_input):
	dir_stack = [Directory("/")]
	for line in puzzle_input:
		curr_dir = dir_stack[-1]
		args = line.split()
		if len(args) == 3:
			dirname = args[2]
			if dirname == "..":
				dir_stack.pop()
			else:
				curr_dir.add_dir(dirname)
				dir_stack.append(curr_dir.dirs[dirname])
		elif " ".join(args) == "$ ls":
			continue
		elif args[0] == "dir":
			curr_dir.add_dir(args[1])
		else:
			# line is a file
			file_size, file_name = line.split()
			file_size = int(file_size)
			curr_dir.add_file(file_name, file_size)
	return dir_stack[0]

def get_threshold_directories(file_system, threshold_func):
	all_dirs = file_system.get_subdirs()
	return [dir for dir in all_dirs if threshold_func(dir.get_size())]


file_system = make_file_system(puzzle_input)

# part 1
threshold_directories = get_threshold_directories(file_system, lambda size: size <= 100000)
print(sum([dir.get_size() for dir in threshold_directories]))

# part 2
unused_space = 70000000 - file_system.get_size()
required_space = 30000000 - unused_space
threshold_directories = get_threshold_directories(file_system, lambda size: size >= required_space)
threshold_directories.sort(key=lambda dir: dir.get_size())
print(threshold_directories[0].get_size())
