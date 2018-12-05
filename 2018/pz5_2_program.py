import re
from string import ascii_lowercase

inputsFile = open("pz5_input.txt", "r")
inputs = inputsFile.read()
print("Total inputs: " + str(len(inputs)))

min_polymer = None
min_length = 500000
max_inhibitor = '_'

for unit in ascii_lowercase:
  print("Checking against " + unit + "...")
  modified_input = re.sub("[" + unit + unit.upper() + "]", "", inputs)
  i = 0
  while i < len(modified_input) - 1:
    first = modified_input[i]
    second = modified_input[i + 1]
    if first.lower() == second.lower() and first.isupper() != second.isupper():
      modified_input = modified_input[:i] + modified_input[i+2:]
      if i > 0:
        i -= 1 # backtrack one to see if new adjacent pairs react
    else:
      i += 1
  if len(modified_input) < min_length:
    min_polymer = modified_input
    min_length = len(modified_input)
    max_inhibitor = unit
  
print("Shortest final result: " + min_polymer)
print("Max inihibitor was " + max_inhibitor)
print("Shortest total length: " + str(min_length))