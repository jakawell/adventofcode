inputsFile = open("pz6_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

max_x, max_y, min_x, min_y = 0, 0, 100000, 100000

for input in inputs: # first, determine the constrained area
  x = int(input.split(", ")[0])
  y = int(input.split(", ")[1])
  max_x = max(max_x, x)
  max_y = max(max_y, y)
  min_x = min(min_x, x)
  min_y = min(min_y, y)

MAX_DISTANCE = 10000
safe_area = 0
  
def process_point(point_x, point_y):
  total_distance = 0
  i = 0
  for input in inputs:
    coordinate_x = int(input.split(", ")[0])
    coordinate_y = int(input.split(", ")[1])
    distance = abs(coordinate_x - point_x) + abs(coordinate_y - point_y) # calculate Manhattan distance
    total_distance += distance
    i += 1
    if total_distance >= MAX_DISTANCE:
      break
  if total_distance < MAX_DISTANCE:
    return 1
  else:
    return 0
  
scanning_offset = 13 # how far outside the constrained area will we scan

half_length = int((max_x - min_x) / 2)
half_height = int((max_y - min_y) / 2)
for iteration in range(0, max(half_length, half_height) + scanning_offset): # scan from the center, outward
  changed_coordinates = []
  start_x = min_x + half_length - iteration
  start_y = min_y + half_height - iteration
  iteration_width = iteration * 2
  if iteration_width == 0: # center point
    safe_area += process_point(start_x, start_y)
  else:
    safe_area += process_point(start_x, start_y) # upper left corner
    safe_area += process_point(start_x, start_y + iteration_width) # upper right
    safe_area += process_point(start_x + iteration_width, start_y) # lower left corner
    safe_area += process_point(start_x + iteration_width, start_y + iteration_width) # lower right corner 
    for i in range(1, iteration_width): # all other points in between the corners, surrouding the previous iteration
      safe_area += process_point(start_x + i, start_y) # right side
      safe_area += process_point(start_x + i, start_y + iteration_width) # left side
      safe_area += process_point(start_x, start_y + i) # upper side
      safe_area += process_point(start_x + iteration_width, start_y + i) # lower side

print("The constrained area is from " + str(min_x) + ", " + str(min_y) + " to " + str(max_x) + ", " + str(max_y) + " for a size of " + str((max_x - min_x) * (max_y - min_y)))
print("The safe area has a size of " + str(safe_area))