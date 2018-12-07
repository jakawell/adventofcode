import re

inputsFile = open("pz7_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

all_steps = ""
step_dict = dict()
for input in inputs:
  before = input.split()[1]
  after = input.split()[7]
  if before not in all_steps:
    all_steps += before
  if after not in all_steps:
    all_steps += after
  if before not in step_dict:
    step_dict[before] = after
  else:
    step_dict[before] += after
    
root_options = all_steps
for afters in step_dict.values():
  for after in afters:
    root_options = re.sub(after, "", root_options)

def order_steps(next_steps, step_dict):
  ordered_next_steps = ''.join(sorted(next_steps)) # alphabetize the next steps
  next_step = ""
  for next in ordered_next_steps: # check the next steps to find first that has completed prerequesites
    found = False
    for value in step_dict.values(): 
      if next in value:
        found = True
        break
    if not found:
      next_step = next
      break
  following_steps = ordered_next_steps[1:] # get the rest of the steps sent to the method
  if next_step in step_dict: # if there are other reported steps that come after the next one, get them and add them to the following steps
    following_steps += step_dict[next_step]
    del step_dict[next_step] # remove step from step dictionary 
  following_steps = re.sub(next_step, "", following_steps) # remove any duplicates of the next step
  for step in step_dict.keys(): # remove the current next step from any other step lists
    step_dict[step] = re.sub(next_step, "", step_dict[step])
  if len(following_steps) > 0: # if there are more steps, order them and append them to the next step
    return next_step + order_steps(following_steps, step_dict)
  else:
    return next_step
    
print(order_steps(root_options, step_dict))