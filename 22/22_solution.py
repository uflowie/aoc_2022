# UNFINISHED
import re

with open('22/input.txt', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()


# transition functions
adjacent = lambda x, y, dx, dy: (x, y, dx, dy)
left = lambda x, y, dx, dy: (50 - y, x, -dy, dx)
right = lambda x, y, dx, dy: (y, x, dy, -dx)
upside_down = lambda x, y, dx, dy: (50 - x, 50 - y, -dx, -dy)

faces = [
    # top, right, bottom, left
    [(left, 5), (adjacent, 1), (adjacent, 2), (upside_down, 3)],  # 0
    [(adjacent, 5), (upside_down, 4), (left, 2), (adjacent, 0)],  # 1
    [(adjacent, 0), (right, 1), (adjacent, 4), (right, 3)],  # 2
    [(left, 2), (adjacent, 4), (adjacent, 5), (upside_down, 0)],  # 3
    [(adjacent, 2), (upside_down, 1), (left, 5), (adjacent, 3)],  # 4
    [(adjacent, 3), (right, 4), (adjacent, 1), (right, 0)],  # 5
]


def move(direction, board, position):
    x, y = position
    dx, dy = direction
    next_x, next_y = ((x + dx) % len(board[0]), (y + dy) % len(board))
    while (board[next_y][next_x] == ' '):
        x, y = (next_x, next_y)
        next_x, next_y = ((x + dx) % len(board[0]), (y + dy) % len(board))
    if board[next_y][next_x] == '#':
        return x, y
    return next_x, next_y


def move_part_2(direction, position, board):
    x, y, face = position
    dx, dy = direction
    next_x, next_y = (x + dx, y + dy)
    
    # default case
    transition_function = adjacent
    next_face = face

    if next_x < 0:
        transition_function = faces[face][3][0]
        next_face = faces[face][3][1]
    if next_x > 49:
        transition_function = faces[face][1][0]
        next_face = faces[face][1][1]
    if next_y < 0:
        transition_function = faces[face][0][0]
        next_face = faces[face][0][1]
    if next_y > 49:
        transition_function = faces[face][2][0]
        next_face = faces[face][2][1]
    next_x, next_y = next_x % 50, next_y % 50
    next_x, next_y, next_dx, next_dy = transition_function(next_x, next_y, dx, dy)
    if board[next_face][next_y][next_x] == '#':
        return x, y, dx, dy, face
    else:
        return next_x, next_y, next_dx, next_dy, next_face


def get_square_from_puzzle_input(top_left, puzzle_input):
    square = []
    for y in range(top_left[1], top_left[1] + 50):
        square.append(puzzle_input[y][top_left[0]:top_left[0] + 50])
    return square


def get_password_part_2(puzzle_input):
    # parse input into faces
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    current_direction = 0
    current_position = (0, 0, 0)

    path = puzzle_input[-1]
    path = [int(s) if s.isdigit()
                else s for s in re.findall(r'[RL]|\d+', path)]

    board = [get_square_from_puzzle_input((50, 0), puzzle_input),
                get_square_from_puzzle_input((100, 0), puzzle_input),
                get_square_from_puzzle_input((50, 50), puzzle_input),
                get_square_from_puzzle_input((0, 100), puzzle_input),
                get_square_from_puzzle_input((50, 100), puzzle_input),
                get_square_from_puzzle_input((0, 150), puzzle_input)]


    for instruction in path:
        if instruction == 'R':
            current_direction= (current_direction + 1) % 4
        elif instruction == 'L':
            current_direction= (current_direction - 1) % 4
        else:
            for _ in range(instruction):
                x, y, dx, dy, face= move_part_2(directions[current_direction], current_position, board)
                current_position= (x, y, face)
                current_direction= directions.index((dx, dy))


def get_password(puzzle_input):
    board= puzzle_input[:-2]
    # pad board to the right with spaces to the longest line in board
    max_len= max([len(line) for line in board])
    board= [line.ljust(max_len) for line in board]
    path= puzzle_input[-1]
    path= [int(s) if s.isdigit() else s for s in re.findall(r'[RL]|\d+', path)]

    directions= [(1, 0), (0, 1), (-1, 0), (0, -1)]
    current_direction= 0
    current_position= (puzzle_input[0].index("."), 0)

    for instruction in path:
        if instruction == 'R':
            current_direction= (current_direction + 1) % 4
        elif instruction == 'L':
            current_direction= (current_direction - 1) % 4
        else:
            for _ in range(instruction):
                current_position= move(directions[current_direction], board, current_position)
    final_x, final_y= [i + 1 for i in current_position]
    return 1000 * final_y + 4 * final_x + current_direction






#print(get_password(puzzle_input))
get_password_part_2(puzzle_input)
