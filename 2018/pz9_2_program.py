import sys

inputsFile = open("pz9_input.txt", "r")
inputs = inputsFile.read().split()

players_count = int(inputs[0])
final_marble = int(inputs[6]) * 100
print("Total players: " + str(players_count) + "; final marble: " + str(final_marble))

scores = [0] * players_count
board = [0]
current_index = 0
turn = 0
percentage = 0
sys.stdout.write("\r%.2f%% complete..." % percentage)
sys.stdout.flush()
for new_marble in range(1, final_marble + 1):
  new_percantage = int((new_marble / final_marble) * 10000) / 100
  if new_percantage != percentage:
    percentage = new_percantage
    sys.stdout.write("\r%.2f%% complete..." % percentage)
    sys.stdout.flush()

  if new_marble % 23 == 0: # the "23" case
    scores[turn] += new_marble # current player keeps the marble
    removed_marble = current_index - 7 # get the index of the marble 7 positions counter clockwise
    if removed_marble < 0:
      removed_marble = len(board) + removed_marble
    scores[turn] += board[removed_marble] # add that marble to the current player's score
    del board[removed_marble] # remove the marble
    current_index = removed_marble % len(board)
  else: # normal play case 
    current_index = (current_index + 2) % len(board)
    board.insert(current_index, new_marble)
  
  turn = (turn + 1) % players_count

print("The winning score is " + str(max(scores)))
    