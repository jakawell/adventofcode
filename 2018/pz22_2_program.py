inputsFile = open("pz22_input.txt", "r")
inputs = inputsFile.read().split()
cave_depth = int(inputs[1])
target_x, target_y = int(inputs[3].split(",")[0]), int(inputs[3].split(",")[1])
print("Cave depth: " + str(cave_depth))
print("Target: " + str(target_x) + ", " + str(target_y))

map = []

def check_map(x, y):
  if len(map) > y and len(map[y]) > x:
    return map[y][x]
  return [-1, -1]

def add_to_map(x, y, score):
  for _ in range(y - len(map) + 1): # add new rows if needed
    map.append([])
    for _ in range(len(map[0])):
      map.append([-1, -1])
  if (x + 1) > len(map[0]): # add new columns if needed
    for row in range(len(map)):
      for _ in range(x - len(map[row]) + 1):
        map[row].append([-1, -1])
  map[y][x] = score

def print_map():
  for y in range(len(map)):
    for x in range(len(map[y])):
      type = check_map(x, y)[1]
      if type == 0:
        print(".", end="")
      elif type == 1:
        print("=", end="")
      else:
        print("|", end="")
    print()

def score_area():
  score = 0
  for y in range(target_y + 1):
    for x in range(target_x + 1):
      if y == 0 and x == 0:
        continue
      if y == target_y and x == target_x:
        continue
      score += check_map(x, y)[1]
  return score

def find_type(x, y):
  if check_map(x, y)[0] > 0: # if the value has already been calculated
    return check_map(x, y)

  geo_index = 0
  if x == 0 and y == 0: # cave entrance
    geo_index = 0
  elif x == target_x and y == target_y: # target location
    geo_index = 0
  elif y == 0: # Y index of 0
    geo_index = x * 16807
  elif x == 0: # X index of 0 
    geo_index = y * 48271
  else: # all other cases
    side1 = find_type(x - 1, y)
    side2 = find_type(x, y - 1)
    geo_index = side1[0] * side2[0]

  erosion_level = (geo_index + cave_depth) % 20183
  type = erosion_level % 3
  add_to_map(x, y, [erosion_level, type])

  return [erosion_level, type]

# gear equipped:
# - 2 is climbing gear
# - 1 is torch
# - 0 is neither

def allowed_equipment(type):
  if type == 0:
    return [2, 1]
  elif type == 1:
    return [2, 0]
  else:
    return [1, 0]

def can_enter(from_x, from_y, to_x, to_y, equipped):
  from_type = find_type(from_x, from_y)[1]
  to_type = find_type(to_x, to_y)[1]
  if len(list(set(allowed_equipment(from_type) & set(allowed_equipment(to_type))))): # if there is an intersection of allowed equipment between 
    return True
  return False

shortest_path = -1

def shortest_path_to_target(from_x, from_y, equipped, previous_path, previous_path_score):
  global shortest_path

  current_path_score = 
  for iterator in range(4):
    x, y = from_x, from_y
    if iterator % 2 != 0 and iterator < 2:
      y -= 1
    else:
      y += iterator % 2
    offset_iterator = iterator + 1
    if offset_iterator % 2 != 0 and offset_iterator > 2:
      x -= 1
    else:
      x += offset_iterator % 2
    name = str(x) + "," + str(y)
    if name not in previous_path:


  north_x, north_y = from_x, from_y - 1
  north_x_name = str(north_x) + "," + str(north_y)
  if north_x_name not in previous_path:



find_type(target_x + 1, target_y + 1)
# print_map()
print("The score of the target area is " + str(score_area()))