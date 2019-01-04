inputsFile = open("pz22_input.txt", "r")
inputs = inputsFile.read().split()
cave_depth = int(inputs[1])
target_x, target_y = int(inputs[3].split(",")[0]), int(inputs[3].split(",")[1])
print("Cave depth: " + str(cave_depth))
print("Target: " + str(target_x) + ", " + str(target_y))

map_width = target_x + 5
map_height = target_y + 5
map = []
for height in range(map_height + 1):
  map.append([])
  for width in range(map_width + 1):
    map[height].append([-1, -1])

def print_map():
  for y in range(len(map)):
    for x in range(len(map[y])):
      type = map[y][x][1]
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
      score += map[y][x][1]
  return score

def find_type(x, y):
  if map[y][x][0] > 0: # if the value has already been calculated
    return map[y][x]

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
  map[y][x] = [erosion_level, type]

  return [erosion_level, type]

find_type(map_width, map_height)
# print_map()
print("The score of the target area is " + str(score_area()))