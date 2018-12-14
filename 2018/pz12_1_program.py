import re

inputsFile = open("pz12_input.txt", "r")
inputs = inputsFile.read().split("\n")
initial_state = inputs[0].split()[2]
raw_rules = inputs[2:]
print("Initial state length: " + str(len(initial_state)))
print("Rule count: " + str(len(raw_rules)))

grow_rules = []
for rule in raw_rules:
  split_rule = rule.split()
  if split_rule[2] == "#":
    grow_rules.append(re.sub("\.", " ", split_rule[0]))
    
max_generation = 20
first_index = 0
for pot in range(len(initial_state)):
  if initial_state[pot] == "#":
    first_index = pot
    break
state = re.sub("\.", " ", initial_state).strip()

print(str(0) + ": " + ("." * (3 - first_index)) + re.sub(" ", ".", state) + "\t\tFirst index: " + str(first_index))

for generation in range(1, max_generation + 1):
  state = "    " + state + "    " # add extra empty pots to the beginning and end
  new_state = ""
  new_first_index = None
  for pot in range(2, len(state) - 2):
    state_set = state[pot - 2:pot + 3]
    if state_set in grow_rules:
      new_state += "#"
      if new_first_index is None:
        new_first_index = pot - 4 + first_index
    else:
      new_state += " "
  state = new_state.strip()
  first_index = new_first_index
  print(str(generation) + ": " + ("." * (3 + first_index)) + re.sub(" ", ".", state) + "\t\tFirst index: " + str(first_index))
  
final_score = 0
for pot in range(len(state)):
  if state[pot] == "#":
    final_score += first_index + pot
    
print("The final score is " + str(final_score))
  