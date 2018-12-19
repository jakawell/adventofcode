inputsFile = open("pz17_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

def parse_vein(descriptor):
  x = []
  y = []
  sides = descriptor.split(", ")
  for i in range(2):
    vals = sides[i].split("=")
    nums = vals[1].split("..")
    for num in nums:
      if vals[0] == "x":
        x.append(int(num))
      else:
        y.append(int(num))
  return [x, y]
  
def print_map(map):
  for row in map:
    for col in row:
      print(col, end="")
    print()

def write_map(file_name, map):
  text = ""
  for row in map:
    for col in row:
      if col == ".":
        text += " "
      else:
        text += col
    text += "\n"
  file = open(file_name, "w")
  file.write(text)

min_x, max_x = 100000, 0
min_y, max_y = 100000, 0

for input_line in inputs:
  vein = parse_vein(input_line)
  if min(vein[0]) < min_x:
    min_x = min(vein[0])
  if max(vein[0]) > max_x:
    max_x = max(vein[0])
  if min(vein[1]) < min_y:
    min_y = min(vein[1])
  if max(vein[1]) > max_y:
    max_y = max(vein[1])
    
print("Corners (x, y): (" + str(min_x) + ", " + str(min_y) + ") to (" + str(max_x) + ", " + str(max_y) + ")")

map = []
for depth in range(max_y + 2):
  map.append(["."] * (max_x - min_x + 1 + 2)) # include an extra x on each side
    
for input_line in inputs:
  vein = parse_vein(input_line)
  for y in range(min(vein[1]), max(vein[1]) + 1):
    for x in range(min(vein[0]) + 1, max(vein[0]) + 1 + 1):
      x = x - min_x
      map[y][x] = "#"
      
start_x, start_y = 500, 0
map[start_y][start_x - min_x + 1] = "+"
sources = [[start_x - min_x + 1, min_y - 1]]

# write_map("pz17_start_map.txt", map)

changes = True
while changes:
  changes = False
  source_index = 0
  while source_index < len(sources):
    source_x, source_y = sources[source_index][0], sources[source_index][1] + 1
    source_index += 1
    for depth in range(source_y, max_y + 1):
      col = source_x
      if map[depth][col] == "|": # if we hit a dropoff marker, the source can be skipped (it's already been handled)
        break
      elif map[depth][col] not in "~#": # if we don't reach more water or ground, we need to keep dropping
        if map[depth][col] != "*":
          changes = True
          map[depth][col] = "*"
        continue
      else: # we hit resting water or ground
        y = depth - 1
        changes = True
        map[y][col] = "~"
        if [col, y] in sources:
          sources.remove([col, y])
        wall_left, wall_right, dropoff = False, False, False
        x_additive = 0
        while (not wall_left or not wall_right) and not dropoff:
          if x_additive >= 0:
            x_additive = x_additive + 1
            if wall_right:
              x_additive = x_additive * -1
              continue
          else:
            if wall_left:
              x_additive = x_additive * -1
              continue
          x = col + x_additive
          if map[y][x] == "#": # hit a wall
            if x_additive > 0:
              wall_right = True
            else:
              wall_left = True
          elif map[y + 1][x] not in "~#": # over an empty gap 
            changes = True
            map[y][x] = "|"
            sources.append([x, y])
            dropoff = True
          else:
            changes = True
            map[y][x] = "~"
          x_additive = x_additive * -1
        if dropoff:
          x_additive = x_additive * -1
          direction = 1 if x_additive < 0 else -1
          x_additive += direction
          while map[y][col + x_additive] not in "#":
            changes = True
            map[y][col + x_additive] = "|"
            if map[y + 1][col + x_additive] not in "~#":
              sources.append([col + x_additive, y])
              break
            x_additive += direction
        break
  # print_map(map)
  # print("Sources:")
  # for source in sources:
  #   print("- " + str(source))
  # print()
  # input("Press ENTER to continue...")
# print_map(map)

wet_cells = 0
retained_water_cells = 0
for row in map:
  for col in row:
    if col == "~":
      wet_cells += 1
      retained_water_cells += 1
    if col == "|" or col == "*":
      wet_cells += 1

# write_map("pz17_end_map.txt", map)
print("Done. Number of damp squares is " + str(wet_cells) + " and the number of retained water cells is " + str(retained_water_cells))