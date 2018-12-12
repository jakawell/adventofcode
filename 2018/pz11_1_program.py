inputsFile = open("pz11_input.txt", "r")
serial_number = int(inputsFile.read())
print("Input: " + str(serial_number))

grid_width, grid_height = 300, 300
selector_width, selector_height = 3, 3
half_selector_width = int(selector_width / 2)
half_selector_height = int(selector_height / 2)

cells = []
for i in range(grid_height):
  cells.append([0] * grid_width)
max_score, max_score_x, max_score_y = 0, 0, 0

def calculate_power_level(x, y, serial_number):
  x = x + 1
  y = y + 1
  rack_id = x + 10
  raw_level = ((rack_id * y) + serial_number) * rack_id
  return abs(int(raw_level / 100) % 10) - 5

for add_y in range(0, selector_height - 1): # initalize the upper corner of the grid
  for add_x in range(0, selector_width - 1): 
    cells[add_y][add_x] = calculate_power_level(add_x, add_y, serial_number)

for y in range(half_selector_height, grid_height - half_selector_height):
  for x in range(half_selector_width, grid_width - half_selector_width):  
    for add_x in range(x - half_selector_width, x + half_selector_width + 1): # add the scores below the selected cell
      cells[y + 1][add_x] = calculate_power_level(add_x, y + 1, serial_number)
    for add_y in range(y - half_selector_height, y + half_selector_height): # add the scores right of the selected cell
      cells[add_y][x + 1] = calculate_power_level(x + 1, add_y, serial_number)
    
    cell_score = 0
    for score_y in range(y - half_selector_height, y + half_selector_height + 1):
      for score_x in range(x - half_selector_width, x + half_selector_width + 1):
        cell_score += cells[score_y][score_x]
    if cell_score > max_score:
      max_score = cell_score
      max_score_x = x
      max_score_y = y
      
    
print("The highest power level is " + str(max_score) + " centered at (one-based) coordinate " + str(max_score_x - half_selector_width + 1) + "," + str(max_score_y - half_selector_height + 1))