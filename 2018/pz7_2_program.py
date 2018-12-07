import re
import string

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
    
second = 0
worker_count = 5
base_task_time = 60
working_tasks = ""
workers = []
for i in range(0, worker_count):
  workers.append(["", 0])
next_steps = root_options
while len(next_steps) > 0 or len(working_tasks) > 0:
  for worker in workers: # complete tasks
    worker_task = worker[0]
    worker_task_remaining = worker[1]
    worker[1] -= 1
    if worker[1] <= 0:
      if len(worker_task) > 0: # mark the step as completed
        working_tasks = re.sub(worker_task, "", working_tasks) # remove from active tasks
        if worker_task in step_dict:
          next_steps += step_dict[worker_task] # add the following steps to upcoming tasks
          del step_dict[worker_task] # remove the task from the step dictionary 
        for step in step_dict.keys(): # remove the completed step from any other step lists
          step_dict[step] = re.sub(worker_task, "", step_dict[step])
      worker[0] = ""
      
  for worker in workers: # assign tasks
    if len(worker[0]) == 0: # check if a new task is available
      ordered_next_steps = ''.join(sorted(next_steps)) # alphabetize the next steps
      next_step = None
      for next in ordered_next_steps: # check the next steps to find first that has completed prerequesites
        found = False
        if next in working_tasks:
          found = True
          break
        for value in step_dict.values(): 
          if next in value:
            found = True
            break
        if not found:
          next_step = next
          break
      if next_step is not None:
        working_tasks += next_step
        next_steps = re.sub(next_step, "", next_steps)
        worker[0] = next_step
        worker[1] = string.ascii_uppercase.index(next_step) + 1 + base_task_time
        #print("Assigning task " + worker[0] + " with time of " + str(worker[1]))
      
  log = str(second) + ":\t"
  for worker in workers:
    if len(worker[0]) > 0:
      log += worker[0] + "\t"
    else:
      log += "*" + "\t"
  log += next_steps
  print(log)
  second += 1

print("Total time: " + str(second - 1))
  