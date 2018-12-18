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

min_x, max_x = 100000, 0
min_y, max_y = 100000, 0

for input in inputs:
  vein = parse_vein(input)
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
for depth in range(max_y + 1):
  map.append(["."] * (max_x - min_x + 1))
    
for input in inputs:
  vein = parse_vein(input)
  for y in range(min(vein[1]), max(vein[1]) + 1):
    for x in range(min(vein[0]), max(vein[0]) + 1):
      x = x - min_x
      map[y][x] = "#"
      
start_x, start_y = 500, 0
map[start_y][start_x - min_x] = "+"
print_map(map)
print()

for drop in range(4):
  for depth in range(max_y):
    col = start_x - min_x
    if map[depth][col] not in "~#":
      continue
    else:
      y = depth - 1
      map[y][col] = "~"
      x = col - 1
      while map[y][x] not in "~#":
        map[y][x] = "~"
        x -= 1
      x = col + 1
      while map[y][x] not in "~#":
        map[y][x] = "~"
        x += 1
      break
  print_map(map)
  print()
