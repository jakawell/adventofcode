import re

inputsFile = open("pz4_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

def is_time_less(first_time, second_time):
  first = int(re.sub("[^0-9]", "", first_time.split("]")[0]))
  second = int(re.sub("[^0-9]", "", second_time.split("]")[0]))
  return first < second

def quicksort_partition(start, end):
  pivot = inputs[end]
  i = start
  for j in range(start, end):
    if is_time_less(inputs[j], pivot):
      if i != j:
        tmp = inputs[i]
        inputs[i] = inputs[j]
        inputs[j] = tmp
      i += 1
  tmp = inputs[i]
  inputs[i] = inputs[end]
  inputs[end] = tmp
  return i

def quicksort(start, end):
  if start < end:
    p = quicksort_partition(start, end)
    quicksort(start, p - 1)
    quicksort(p + 1, end)
    
quicksort(0, len(inputs) - 1)

current_guard = None
fell_asleep_time = None

guard_sleep_times = dict()
max_sleep_time = 0
max_sleep_guard = None

for input in inputs:
  #print(re.sub("[^0-9]", "", input.split("]")[0]))
  split_input = input.split()
  if split_input[2] == "Guard": # "begins shift" note
    current_guard = split_input[3][1:]
  elif split_input[2] == "falls": # "falls asleep" note
    fell_asleep_time = int(split_input[1].split(":")[1][:-1])
  elif split_input[2] == "wakes": # "wakes up" note
    wake_up_time = int(split_input[1].split(":")[1][:-1])
    if current_guard not in guard_sleep_times:
      guard_sleep_times[current_guard] = [0] * 61 # each of the 60 minutes from 00:00 to 00:59, plus a final "total" column
    for minute in range(fell_asleep_time, wake_up_time):
      guard_sleep_times[current_guard][minute] += 1
      guard_sleep_times[current_guard][60] += 1 # increment the total
    if guard_sleep_times[current_guard][60] > max_sleep_time:
      max_sleep_time = guard_sleep_times[current_guard][60]
      max_sleep_guard = current_guard

most_sleep_times = guard_sleep_times[max_sleep_guard]      
most_sleep_minute = most_sleep_times.index(max(guard_sleep_times[max_sleep_guard][:-1]))

print("The sleepiest guard is #" + max_sleep_guard + " who is most often asleep at the " + str(most_sleep_minute) + " minute.")
print("The multiplied answer is " + str(int(max_sleep_guard) * most_sleep_minute))