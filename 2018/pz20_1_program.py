inputsFile = open("pz20_input.txt", "r")
inputs = inputsFile.read()
print("Total inputs: " + str(len(inputs)))

center_x, center_y = 1, 1
map = [["#", "?", "#"], 
       ["?", "X", "?"], 
       ["#", "?", "#"]]

room_paths = dict()

def print_map():
  for y in range(len(map)):
    for x in range(len(map[y])):
      print(map[y][x], end="")
    print()

def clean_map():
  for y in range(len(map)):
    for x in range(len(map[y])):
      if map[y][x] == "?":
        if y > 0 and y < len(map) - 1 and map[y - 1][x] == "#" and map[y + 1][x] == "#":
          map[y][x] = "#"
        elif x > 0 and x < len(map[y]) - 1 and map[y][x - 1] == "#" and map[y][x + 1] == "#":
          map[y][x] = "#"
        else:
          map[y][x] = " "

def add_direction(direction, from_x, from_y, current_path):
  absolute_x, absolute_y = from_x, from_y
  from_x, from_y = from_x * 2, from_y * 2 # the internal map counts doors as points, so room offsets need to be doubled
  global center_x
  global center_y
  global room_paths

  x_add, y_add = 0, 0
  if direction == "N":
    y_add -= 1
  elif direction == "E":
    x_add += 1
  elif direction == "S":
    y_add += 1
  elif direction == "W":
    x_add -= 1
  
  new_x, new_y = center_x + from_x + x_add, center_y + from_y + y_add
  
  if new_y == 0:
    map.insert(0, ["?"] * len(map[center_y]))
    map.insert(0, ["?"] * len(map[center_y]))
    center_y += 2
  elif new_x == len(map[new_y]) - 1:
    for row in range(len(map)):
      map[row].append("?")
      map[row].append("?")
  elif new_y == len(map) - 1:
    map.append(["?"] * len(map[center_y]))
    map.append(["?"] * len(map[center_y]))
  elif new_x == 0:
    for row in range(len(map)):
      map[row].insert(0, "?")
      map[row].insert(0, "?")
    center_x += 2

  new_x, new_y = center_x + from_x + x_add, center_y + from_y + y_add # reset the new location based on the new center

  new_room_name = str(absolute_x + x_add) + "," + str(absolute_y + y_add)
  if map[new_y + y_add][new_x + x_add] == ".": 
    if len(room_paths[new_room_name]) > len(current_path): # if the room already exists and the current path is shorter to it
      room_paths[new_room_name] = current_path[:] # change the stored path to this room to the new path
      for room_path_key in room_paths.keys(): # find any other rooms that include this room in their path and update them with the new shorter start
        if new_room_name in room_paths[room_path_key]:
          index_of_room = room_paths[room_path_key].index(new_room_name)
          room_paths[room_path_key] = current_path[:] + room_paths[room_path_key][index_of_room:]
  else: # if the room is new, add it to the path list
    room_paths[new_room_name] = current_path[:]
  
  if map[new_y][new_x] == "?":
    map[new_y][new_x] = "|" if y_add == 0 else "-" # add door
    map[new_y + y_add][new_x + x_add] = "." # add room

    map[new_y + y_add + 1][new_x + x_add - 1] = "#" # add corner
    map[new_y + y_add + 1][new_x + x_add + 1] = "#" # add corner
    map[new_y + y_add - 1][new_x + x_add - 1] = "#" # add corner
    map[new_y + y_add - 1][new_x + x_add + 1] = "#" # add corner
  
  new_path = current_path[:]
  new_path.append(new_room_name)
  return [absolute_x + x_add, absolute_y + y_add, new_path]

start_stack = [[0, 0, []]]
for input in inputs:
  if input == "^":
    continue
  elif input == "$":
    break
  elif input == "(":
    start_stack.append(start_stack[-1])
  elif input == "|":
    start_stack.pop()
    start_stack.append(start_stack[-1])
  elif input == ")":
    start_stack.pop()
  else:
    start_stack[-1] = add_direction(input, start_stack[-1][0], start_stack[-1][1], start_stack[-1][2])
  
# clean_map()
# print_map()
furthest_room = ""
longest_path = 0
long_path_count = 0
for room_key in room_paths.keys():
  if len(room_paths[room_key]) + 1 >= 1000:
    long_path_count += 1
  if len(room_paths[room_key]) > longest_path:
    furthest_room = room_key
    longest_path = len(room_paths[room_key])
print("The longest path is " + str(longest_path + 1) + " at " + furthest_room + " (relative to the start).")
print("There are " + str(long_path_count) + " rooms at least 1000 doors away.")