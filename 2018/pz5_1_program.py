inputsFile = open("pz5_input.txt", "r")
inputs = inputsFile.read()
print("Total inputs: " + str(len(inputs)))

i = 0
while i < len(inputs) - 1:
  first = inputs[i]
  second = inputs[i + 1]
  if first.lower() == second.lower() and first.isupper() != second.isupper():
    inputs = inputs[:i] + inputs[i+2:]
    if i > 0:
      i -= 1 # backtrack one to see if new adjacent pairs react
  else:
    i += 1
  
print("Final result: " + inputs)
print("Total length: " + str(len(inputs)))