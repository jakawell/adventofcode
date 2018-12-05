inputsFile = open("pz3_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

taken_inches = dict()
total_double_taken = 0
intact_id = None

for input in inputs:
  split_input = input.split()
  x_start = int(split_input[2].split(",")[0])
  y_start = int(split_input[2].split(",")[1][:-1])
  x_length = int(split_input[3].split("x")[0])
  y_length = int(split_input[3].split("x")[1])
  for x_index in range(x_length):
    for y_index in range(y_length):
      point = str(x_start + x_index) + "X" + str(y_start + y_index)
      if point not in taken_inches:
        taken_inches[point] = 1
      elif taken_inches[point] == 1: # this is the first time the point is used by a second elf, so we should add to the list
        total_double_taken += 1
        taken_inches[point] += 1
      else:
        taken_inches[point] += 1
        
for input in inputs:
  is_intact = True
  split_input = input.split()
  x_start = int(split_input[2].split(",")[0])
  y_start = int(split_input[2].split(",")[1][:-1])
  x_length = int(split_input[3].split("x")[0])
  y_length = int(split_input[3].split("x")[1])
  for x_index in range(x_length):
    for y_index in range(y_length):
      point = str(x_start + x_index) + "X" + str(y_start + y_index)
      if taken_inches[point] != 1:
        is_intact = False
        break
  if is_intact:
    print("Found intact claim!")
    intact_id = split_input[0]
        
print("Total points taken by two or more: " + str(total_double_taken))
if intact_id is not None:
  print("Intact ID is " + intact_id)