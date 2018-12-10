import re
import copy

inputsFile = open("pz10_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

points = []
for point in inputs:
  split = re.split("[<,>]", point)
  points.append([[int(split[1]), int(split[2])], [int(split[4]), int(split[5])]])
  
def print_points(points):
  min_x, max_x = 10000000, 0
  min_y, max_y = 10000000, 0
  for point in points:
    min_x = min(min_x, point[0][0])
    max_x = max(max_x, point[0][0])
    min_y = min(min_y, point[0][1])
    max_y = max(max_y, point[0][1])
  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      found_point = False
      for point in points:
        if point[0][0] == x and point[0][1] == y:
          found_point = True
          break
      if found_point:
        print("# ", end='')
      else:
        print("  ", end='')
    print()
    
def measure_area(points):
  min_x, max_x = 10000000, 0
  min_y, max_y = 10000000, 0
  for point in points:
    min_x = min(min_x, point[0][0])
    max_x = max(max_x, point[0][0])
    min_y = min(min_y, point[0][1])
    max_y = max(max_y, point[0][1])
  return (max_x - min_x) * (max_y - min_y)
  
last_area = -1
for i in range(100000):
  last_state = copy.deepcopy(points)
  for p in range(0, len(points)):
    points[p][0][0] += points[p][1][0]
    points[p][0][1] += points[p][1][1]
  new_area = measure_area(points)
  if new_area > last_area and last_area != -1:
    print_points(last_state)
    print("Found in " + str(i) + " seconds.")
    break
  else:
    last_area = new_area
  