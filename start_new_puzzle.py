import datetime
import os
import sys
import requests

day = "24"

# get input.txt from aoc website
session_cookie = sys.argv[1]
input_url = f"https://adventofcode.com/2022/day/{day}/input"
cookies = {
    "session": session_cookie
}
response = requests.get(input_url, cookies=cookies)
status_code = response.status_code
if status_code != 200:
    print(f"failed to request input file from aoc url, expected http status 200, received {status_code}")
    sys.exit(0)
input_file_content = response.text

os.mkdir(day)

# create file containing the code for the problem, including the default way to read in the puzzle input
with open(os.path.join(day, f"{day}_solution.py"), "w") as solution_file:
    solution_file.write(f"with open('{day}/input.txt', 'r') as input_file:\n")
    solution_file.write("\tpuzzle_input = input_file.read().splitlines()\n")

with open(os.path.join(day, "input.txt"), "w") as input_file:
    input_file.write(input_file_content)

