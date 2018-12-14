import sys

inputsFile = open("pz13_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total map rows: " + str(len(inputs)))

turn_states = dict() # stores the current locations of carts and what their next turn will be

collisions = []
last_locations = dict()
tick = 0
cart_count = 2
last_cart = None
last_cart_count = 100
while cart_count > 1:
  cart_count = 0

  ignore = []
  for row in range(len(inputs)):
    row_input = inputs[row]
    for col in range(len(row_input)):
      state_string = str(row) + "," + str(col)
      if state_string in ignore: # check if this element has already been moved on this tick
        continue
      
      row_add, col_add, dir = 0, 0, 0 
      if row_input[col] == "^": # get the new location and current direction
        row_add = -1
        dir = 0
      elif row_input[col] == ">":
        col_add = 1
        dir = 1
      elif row_input[col] == "v":
        row_add = 1
        dir = 2
      elif row_input[col] == "<":
        col_add = -1
        dir = 3
      else:
        continue
        
      cart_count += 1
      
      new_row, new_col, new_dir = row + row_add, col + col_add, dir
      new_state_string = str(new_row) + "," + str(new_col)
      new_location = inputs[new_row][new_col]
      is_collision = False
      
      if new_location in "^><vX": # if new location is another cart (collision)
        is_collision = True
        cart_count -= 2
        collisions.append(new_state_string)
      elif new_location == "/": # if new location is right curve
        if dir % 2 == 0:
          new_dir = dir + 1
        else:
          new_dir = dir - 1
      elif new_location == "\\": # if new location is left curve
        if dir % 2 == 0:
          new_dir = (dir - 1) % 4
        else:
          new_dir = (dir + 1) % 4
      elif new_location == "+": # if new location is intersection 
        if state_string not in turn_states:
          turn_states[state_string] = 0
        new_dir = (dir + (turn_states[state_string] - 1)) % 4
        turn_states[state_string] = (turn_states[state_string] + 1) % 3
      
      if state_string in turn_states: # change the turn state key to new location 
        if not is_collision:
          turn_states[new_state_string] = turn_states[state_string]
        del turn_states[state_string]
      
      if state_string in last_locations: # if we have a record of the last location 
        inputs[row] = inputs[row][:col] + last_locations[state_string] + inputs[row][col + 1:]
        del last_locations[state_string]
      else: # if we don't have a record, we have to make an educated guess
        is_up, is_right, is_down, is_left = False, False, False, False # check the surrounding tracks to reset the current location
        if row > 0:
          up = inputs[row - 1][col]
          if up in "|/\\+^>v<X":
            is_up = True
        if col < len(row_input) - 1:
          right = inputs[row][col + 1]
          if right in "-/\\+^>v<X":
            is_right = True
        if row < len(inputs) - 1:
          down = inputs[row + 1][col]
          if down in "|/\\+^>v<X":
            is_down = True
        if col > 0:
          left = inputs[row][col - 1]
          if left in "-/\\+^>v<X":
            is_left = True
        
        if is_up and is_right and is_down and is_left: # update the current cart position to the empty track value 
          inputs[row] = inputs[row][:col] + "+" + inputs[row][col + 1:]
        elif (is_up and is_right and not is_down and not is_left) or (is_down and is_left and not is_up and not is_right):
          inputs[row] = inputs[row][:col] + "\\" + inputs[row][col + 1:]
        elif (is_up and is_left and not is_down and not is_right) or (is_down and is_right and not is_up and not is_left):
          inputs[row] = inputs[row][:col] + "/" + inputs[row][col + 1:]
        elif is_left and is_right:
          inputs[row] = inputs[row][:col] + "-" + inputs[row][col + 1:]
        elif is_up and is_down:
          inputs[row] = inputs[row][:col] + "|" + inputs[row][col + 1:]
          
      if not is_collision: # save the current empty track char before replacing the cart
        last_locations[new_state_string] = inputs[new_row][new_col]
        
      if is_collision: # update the new location 
        inputs[new_row] = inputs[new_row][:new_col] + last_locations[new_state_string] + inputs[new_row][new_col + 1:]
        del last_locations[new_state_string]
      else:
        inputs[new_row] = inputs[new_row][:new_col] + "^>v<"[new_dir] + inputs[new_row][new_col + 1:]
      ignore.append(new_state_string)
      
      if not is_collision:
        last_cart = new_state_string
  
  if cart_count != last_cart_count:
    last_cart_count = cart_count
    sys.stdout.write("\rRunning... %d carts remain." % cart_count)
    sys.stdout.flush()
  tick += 1
    
print("\nFinished. At tick " + str(tick))
for input in inputs:
  print(input)
print("Last cart is at " + last_cart.split(',')[1] + "," + last_cart.split(',')[0])