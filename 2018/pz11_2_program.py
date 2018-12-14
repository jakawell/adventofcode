import sys

inputsFile = open("pz11_input.txt", "r")
serial_number = int(inputsFile.read())
print("Input: " + str(serial_number))

grid_width, grid_height = 300, 300
selector_width, selector_height = 1, 1
half_selector_width = int(selector_width / 2)
half_selector_height = int(selector_height / 2)

cells = []
for i in range(grid_height):
  cells.append([0] * grid_width)
max_score, max_score_x, max_score_y, max_score_selector = 0, 0, 0, 0

scores = []
for i in range(grid_height):
  scores.append([0] * ((grid_height - i) ** 2))

def calculate_power_level(x, y, serial_number):
  x = x + 1
  y = y + 1
  rack_id = x + 10
  raw_level = ((rack_id * y) + serial_number) * rack_id
  return abs(int(raw_level / 100) % 10) - 5  
  
for y in range(grid_height):
  percent_complete = int(y / grid_height * 100)
  sys.stdout.write("\r%d%% complete..." % percent_complete)
  sys.stdout.flush()
  for x in range(grid_width):
    score = calculate_power_level(x, y, serial_number)
    for i in range(grid_height):
      w = grid_width - i
      total_length = w ** 2
      
      for i_y in range(i + 1):
        for i_x in range(i + 1):
          x_n = (x - i_x)
          if x_n >= 0 and x_n < w:
            index = ((y - i_y) * w) + x_n
            if index >= 0 and index < total_length:
              scores[i][index] += score

print("Scoring...")
max_score, max_selector, max_selector_location = 0, 0, 0
for selector in range(len(scores)):
  for location in range(len(scores[selector])):
    if scores[selector][location] > max_score:
      max_score = scores[selector][location]
      max_selector = selector
      max_selector_location = location
print("Max score is " + str(max_score))
    

# while selector_width <= grid_width:
  # percent_complete = int(selector_width / grid_width * 100)
  # sys.stdout.write("\r%d%% complete..." % percent_complete)
  # sys.stdout.flush()
  # for y in range(half_selector_height, grid_height - half_selector_height):
    # for x in range(half_selector_width, grid_width - half_selector_width):
      # if selector_width == 1:
        # cell_score = calculate_power_level(x, y, serial_number)
        # cells[y][x] = cell_score
        # if cell_score > max_score:
          # max_score = cell_score
          # max_score_x = x
          # max_score_y = y
          # max_score_selector = selector_width
      # else:
        # cell_score = 0
        # for score_y in range(y - half_selector_height, y + half_selector_height + 1):
          # for score_x in range(x - half_selector_width, x + half_selector_width + 1):
            # cell_score += cells[score_y][score_x]
            # if cell_score > max_score:
              # max_score = cell_score
              # max_score_x = x
              # max_score_y = y
              # max_score_selector = selector_width
      
  # selector_width += 1
  # selector_height += 1
  # half_selector_width = int(selector_width / 2)
  # half_selector_height = int(selector_height / 2)
  
    
# print("The highest power level is " + str(max_score) + " centered at (one-based) coordinate " + str(max_score_x - int((selector_width - 1) / 2) + 1) + "," + str(max_score_y - int((selector_height - 1) / 2) + 1) + "," + str(max_score_selector))