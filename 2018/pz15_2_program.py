import copy
import math

inputsFile = open("pz15_input.txt", "r")
inputs_raw = inputsFile.read().split("\n")
print("Total map rows: " + str(len(inputs_raw)))

def generate_loc_key(row, col):
  return str(row) + "," + str(col)

def can_move(row, col):
  if row > 0 and inputs[row - 1][col] == ".":
    return True
  if row < len(inputs) - 1 and inputs[row + 1][col] == ".":
    return True
  if col > 0 and inputs[row][col - 1] == ".":
    return True
  if col < len(inputs[row]) - 1 and inputs[row][col + 1] == ".":
    return True
  return False
  
def find_enemy(inputs, combatants, paths, global_ignore, self_type):
  new_paths = []
  target_paths = []
  found_something = False
  for path in paths:
    row, col = int(path[-1].split(",")[0]), int(path[-1].split(",")[1]) # check end of path
    for row_index in range(3):
      path_row = row + row_index - 1
      for path_col in range(col - (row_index % 2), col + (row_index % 2) + 1):
        path_key = generate_loc_key(path_row, path_col)
          
        if (path_row != row or path_col != col) and path_key not in global_ignore:
          if path_row < 0 or path_row >= len(inputs) or path_col < 0 or path_col >= len(inputs[row]):
            continue
          elif inputs[path_row][path_col] == ".": # can move
            new_path = path[:]
            new_path.append(path_key)
            new_paths.append(new_path)
            global_ignore.append(path_key)
            found_something = True
          elif inputs[path_row][path_col] in "EG" and inputs[path_row][path_col] != self_type: # is enemy
            new_path = path[:]
            new_path.append(path_key)
            target_paths.append(new_path)
            global_ignore.append(path_key)
            found_something = True
  
  if len(target_paths): # find the first target in reading order
    if len(target_paths[0]) == 2: # the target path is only two, meaning the enemy is immediately proximate and should be attacked
      weakest, weakest_hp, weakest_row, weakest_col = None, 201, 0, 0
      for target_path in range(0, len(target_paths)):
        target = target_paths[target_path][-1]
        new_target_row, new_target_col = target.split(",")[0], target.split(",")[1]
        if combatants[target][1] < weakest_hp or (combatants[target][1] == weakest_hp and new_target_row <= weakest_row and new_target_col < weakest_col):
          weakest = target
          weakest_hp = combatants[target][1]
          weakest_row, weakest_col = new_target_row, new_target_col
      return [ "a", weakest]
    else:
      target_row, target_col = target_paths[0][1].split(",")[0], target_paths[0][1].split(",")[1] # take first step of first target path 
      for target_path in range(1, len(target_paths)):
        new_target_row, new_target_col = target_paths[target_path][1].split(",")[0], target_paths[target_path][1].split(",")[1]
        if new_target_row <= target_row and new_target_col < target_col:
          target_row, target_col = new_target_row, new_target_col
      return [ "m", generate_loc_key(target_row, target_col) ]
  elif not found_something:
    return None
  else:
    return find_enemy(inputs, combatants, new_paths, global_ignore, self_type)
    
def print_map(inputs):
  for row in inputs:
    print(row)

def run_battle(combatants, e_count, g_count, elf_attack):
  inputs = inputs_raw[:]
  
  force_end = False
  round = 0

  while True:
    round += 1
    moved = [] # stores keys of all combatants that have already moved this round
    
    for row in range(len(inputs)): # scan the map for combatants in reading order
      for col in range(len(inputs[0])):
        self = inputs[row][col]
        loc_key = generate_loc_key(row, col)
        if self in "EG" and loc_key not in moved:
          if e_count <= 0 or g_count <= 0:
            force_end = True
            # print("Combat is over in round " + str(round))
            break
          
          self_can_move = True
          is_attackable = True
          
          if self_can_move and is_attackable:
            next_move = find_enemy(inputs, combatants, [[loc_key]], [], self)
            if next_move is not None:
              if next_move[0] == "m":
                next_row, next_col = int(next_move[1].split(",")[0]), int(next_move[1].split(",")[1])
                inputs[row] = inputs[row][:col] + "." + inputs[row][col + 1:]
                inputs[next_row] = inputs[next_row][:next_col] + self + inputs[next_row][next_col + 1:]
                self_combatant = combatants[loc_key]
                del combatants[loc_key]
                combatants[next_move[1]] = self_combatant
                moved.append(next_move[1])
                next_move = find_enemy(inputs, combatants, [[next_move[1]]], [], self)
              else:
                moved.append(loc_key)
              if next_move is not None and next_move[0] == "a":
                if self == "E":
                  combatants[next_move[1]][1] -= elf_attack
                else:
                  combatants[next_move[1]][1] -= 3
                if combatants[next_move[1]][1] <= 0:
                  enemy_row, enemy_col = int(next_move[1].split(",")[0]), int(next_move[1].split(",")[1])
                  if combatants[next_move[1]][0] == "E":
                    e_count -= 1
                  else:
                    g_count -= 1
                  inputs[enemy_row] = inputs[enemy_row][:enemy_col] + "." + inputs[enemy_row][enemy_col + 1:]
                  del combatants[next_move[1]]
            else:
              moved.append(loc_key)
          else:
            moved.append(loc_key)
    if force_end:
      break
    
  total_hp = 0
  for combatant in combatants.keys():
    total_hp += combatants[combatant][1]
  return [ (round * total_hp), ((round - 1) * total_hp), inputs, combatants ]
  

combatants = dict() # stores the coordinates of the combatant as the key, with the value being a tuple: [type ("E" or "G"), HP]
e_count, g_count = 0, 0
for row in range(len(inputs_raw)): # do an initial scan of the map for all combatants
  for col in range(len(inputs_raw[0])):
    if inputs_raw[row][col] in "EG":
      combatants[generate_loc_key(row, col)] = [inputs_raw[row][col], 200]
      if inputs_raw[row][col] == "E":
        e_count += 1
      else:
        g_count += 1


elf_attack = 4
increaser = 1
move = 10 ** increaser
fail_multiplier = 1
last_success_attack, last_success = 0, None
while move != 0:
  elf_attack = elf_attack + move
  scores = run_battle(copy.deepcopy(combatants), e_count, g_count, elf_attack)
  elf_count = 0
  for combatant_key in scores[3].keys():
    if scores[3][combatant_key][0] == "E":
      elf_count += 1
  if elf_count == e_count:
    last_success = scores[:]
    last_success_attack = elf_attack
    fail_multiplier = -1
    increaser = -1
  else:
    fail_multiplier = 1
  
  if increaser > 0:
    increaser += 1
    move = 10 ** increaser
  else:
    next_move = move / 2
    if int(next_move) == 0:
      move = 0
    elif next_move > 0:
      move = abs(math.ceil(next_move)) * fail_multiplier
    elif next_move < 0:
      move = abs(math.floor(next_move)) * fail_multiplier

scores = last_success
print("The minimum attack is " + str(last_success_attack))
print_map(scores[2])
for combatant_key in scores[3].keys():
  print(combatant_key + ": " + str(scores[3][combatant_key]))
# print("Final score: " + str(scores[0]))
print("Final score: " + str(scores[1]))