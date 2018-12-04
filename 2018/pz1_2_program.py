inputsFile = open("pz1_input.txt", "r")
inputs = inputsFile.read().split()
print("Total inputs: " + str(len(inputs)))

result = 0

previous_results = [ 0 ]
found_duplicate = False
first_duplicate = 0

iterations = 0
while not found_duplicate:
  print("Running iteration " + str(iterations) + "... (previous results are up to " + str(len(previous_results)) + ")")
  iterations += 1
  for input in inputs:
    if input[0] == '+':
      result += int(input[1:])
    else:
      result -= int(input[1:])
    for previous in previous_results:
      if result == previous and not found_duplicate:
        print("Found a match!")
        first_duplicate = result
        found_duplicate = True
        break
    previous_results.append(result)

print("First duplicate: " + str(first_duplicate))