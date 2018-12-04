inputsFile = open("pz1_input.txt", "r")
inputs = inputsFile.read().split()
print("Total inputs: " + str(len(inputs)))

result = 0
for input in inputs:
  if input[0] == '+':
    result += int(input[1:])
  else:
    result -= int(input[1:])

print("Result: " + str(result))