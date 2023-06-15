with open('21/input.txt', 'r') as input_file:
	puzzle_input = input_file.read()

# Define a dictionary to store the numbers yelled by each monkey
numbers = {}

# Define a function to compute the number yelled by a monkey
def compute_number(monkey):
  # If the monkey has already yelled its number, return it
  if monkey in numbers:
    return numbers[monkey]
  
  # Get the job of the monkey
  job = jobs[monkey]
  
  # If the job is just a number, store it in the dictionary and return it
  if job.isdigit():
    numbers[monkey] = int(job)
    return numbers[monkey]
  
  # If the job is an operation, compute the numbers yelled by the operands
  operand1, operator, operand2 = job.split()
  number1 = compute_number(operand1)
  number2 = compute_number(operand2)
  
  # Perform the operation and store the result in the dictionary
  if operator == '+':
    result = number1 + number2
  elif operator == '-':
    result = number1 - number2
  elif operator == '*':
    result = number1 * number2
  elif operator == '/':
    result = number1 // number2
  numbers[monkey] = result
  
  # Return the result
  return numbers[monkey]

# Define a dictionary to store the jobs of each monkey
jobs = {}

# Parse the input
lines = puzzle_input.strip().split('\n')
for line in lines:
  monkey, job = line.split(': ')
  jobs[monkey] = job

# Compute the number yelled by the root monkey
result = compute_number("root")

# Print the result
print(result)