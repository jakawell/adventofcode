import sys

inputsFile = open("pz18_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

def print_map(map):
  for row in map:
    for col in row:
      print(col, end="")
    print()

# print("Initial state:")
# print_map(inputs)

max_minute = 1000000000
percentage = 0
for minute in range(max_minute):
  new_percentage = int((minute / max_minute) * 1000000)
  if new_percentage != percentage:
    percentage = new_percentage
    sys.stdout.write("\r%.4f%% complete..." % (percentage / 10000))
    sys.stdout.flush()

  inputs_copy = inputs[:]
  for row in range(len(inputs)):
    for col in range(len(inputs[row])):
      tree_count, lumber_count, open_count = 0, 0, 0
      for row_adj in range(row - 1, row + 2):
        if row_adj >= 0 and row_adj < len(inputs):
          for col_adj in range(col - 1, col + 2):
            if (row_adj != row or col_adj != col) and col_adj >= 0 and col_adj < len(inputs[row]):
              if inputs[row_adj][col_adj] == "|":
                tree_count += 1
              elif inputs[row_adj][col_adj] == "#":
                lumber_count += 1
              elif inputs[row_adj][col_adj] == ".":
                open_count += 1
      if inputs[row][col] == "|" and lumber_count >= 3:
        inputs_copy[row] = inputs_copy[row][:col] + "#" + inputs_copy[row][col + 1:]
      elif inputs[row][col] == "#" and (lumber_count == 0 or tree_count == 0):
        inputs_copy[row] = inputs_copy[row][:col] + "." + inputs_copy[row][col + 1:]
      elif inputs[row][col] == "." and tree_count >= 3:
        inputs_copy[row] = inputs_copy[row][:col] + "|" + inputs_copy[row][col + 1:]
  inputs = inputs_copy
  # print("After " + str(minute + 1) + " minutes:")
  # print_map(inputs)
  # input("Press ENTER...")

tree_total, lumber_total = 0, 0
for row in inputs:
  for col in row:
    if col == "|":
      tree_total += 1
    elif col == "#":
      lumber_total += 1

print("There are " + str(tree_total) + " wooded acres and " + str(lumber_total) + " lumber yards for a resource value of " + str(tree_total * lumber_total))