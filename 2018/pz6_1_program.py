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
  
def process_point(point_x, point_y, coordinate_scores, changed_coordinates):
  closest_coordinates, closest_distance = [], 100000
  i = 0
  for input in inputs:
    coordinate_x = int(input.split(", ")[0])
    coordinate_y = int(input.split(", ")[1])
    distance = abs(coordinate_x - point_x) + abs(coordinate_y - point_y) # calculate Manhattan distance
    if distance < closest_distance:
      closest_coordinates = []
      closest_coordinates.append(i)
      closest_distance = distance
    elif distance == closest_distance:
      closest_coordinates.append(i)
    i += 1

  if len(closest_coordinates) == 1:
    closest_coordinate = closest_coordinates[0]
    coordinate_scores[closest_coordinate] += 1
  # for closest_coordinate in closest_coordinates:
    if closest_coordinate not in changed_coordinates:
      changed_coordinates.append(closest_coordinate)
  
scanning_offset = 13 # how far outside the constrained area will we scan

coordinate_scores = [0] * len(inputs) # contains the number of points closest to each coordinate within the constrained area
changed_coordinates = []
half_length = int((max_x - min_x) / 2)
half_height = int((max_y - min_y) / 2)
for iteration in range(0, max(half_length, half_height) + scanning_offset): # scan from the center, outward
  changed_coordinates = []
  start_x = min_x + half_length - iteration
  start_y = min_y + half_height - iteration
  iteration_width = iteration * 2
  if iteration_width == 0: # center point
    process_point(start_x, start_y, coordinate_scores, changed_coordinates)
  else:
    process_point(start_x, start_y, coordinate_scores, changed_coordinates) # upper left corner
    process_point(start_x, start_y + iteration_width, coordinate_scores, changed_coordinates) # upper right
    process_point(start_x + iteration_width, start_y, coordinate_scores, changed_coordinates) # lower left corner
    process_point(start_x + iteration_width, start_y + iteration_width, coordinate_scores, changed_coordinates) # lower right corner 
    for i in range(1, iteration_width): # all other points in between the corners, surrouding the previous iteration
      process_point(start_x + i, start_y, coordinate_scores, changed_coordinates) # right side
      process_point(start_x + i, start_y + iteration_width, coordinate_scores, changed_coordinates) # left side
      process_point(start_x, start_y + i, coordinate_scores, changed_coordinates) # upper side
      process_point(start_x + iteration_width, start_y + i, coordinate_scores, changed_coordinates) # lower side
  # print("At iteration " + str(iteration) + ": changed " + str(changed_coordinates))

largest_area, largest_area_coordinate = 0, -1
i = 0
for score in coordinate_scores:
  coordinate_x = int(inputs[i].split(", ")[0])
  coordinate_y = int(inputs[i].split(", ")[1])
  if i not in changed_coordinates:
    if score > largest_area:
      largest_area = score
      largest_area_coordinate = i
  i += 1
  
print("The constrained area is from " + str(min_x) + ", " + str(min_y) + " to " + str(max_x) + ", " + str(max_y) + " for a size of " + str((max_x - min_x) * (max_y - min_y)))
print("The largest non-infinite area is " + str(largest_area) + " controlled by point " + str(largest_area_coordinate))