inputsFile = open("pz19_input.txt", "r")
inputs = inputsFile.read().split("\n")
print("Total inputs: " + str(len(inputs)))

def parse_instruction(instruction):
  splits = instruction.split()
  return [splits[0], int(splits[1]), int(splits[2]), int(splits[3])]

def run_command(op, inputs, output, registries):
  if op == "addr":
    registries[output] = registries[inputs[0]] + registries[inputs[1]]
  elif op == "addi":
    registries[output] = registries[inputs[0]] + inputs[1]
    
  elif op == "mulr":
    registries[output] = registries[inputs[0]] * registries[inputs[1]]
  elif op == "muli":
    registries[output] = registries[inputs[0]] * inputs[1]
    
  elif op == "banr":
    registries[output] = registries[inputs[0]] & registries[inputs[1]]
  elif op == "bani":
    registries[output] = registries[inputs[0]] & inputs[1]
    
  elif op == "borr":
    registries[output] = registries[inputs[0]] | registries[inputs[1]]
  elif op == "bori":
    registries[output] = registries[inputs[0]] | inputs[1]
    
  elif op == "setr":
    registries[output] = registries[inputs[0]]
  elif op == "seti":
    registries[output] = inputs[0]
    
  elif op == "gtir":
    registries[output] = 1 if inputs[0] > registries[inputs[1]] else 0
  elif op == "gtri":
    registries[output] = 1 if registries[inputs[0]] > inputs[1] else 0
  elif op == "gtrr":
    registries[output] = 1 if registries[inputs[0]] > registries[inputs[1]] else 0
    
  elif op == "eqir":
    registries[output] = 1 if inputs[0] == registries[inputs[1]] else 0
  elif op == "eqri":
    registries[output] = 1 if registries[inputs[0]] == inputs[1] else 0
  elif op == "eqrr":
    registries[output] = 1 if registries[inputs[0]] == registries[inputs[1]] else 0
    
  return registries

ip_reg = int(inputs[0].split()[1])
ip = 0
registries = [1, 0, 0, 0, 0, 0]

while (ip + 1) < len(inputs): # next instruction is in command set
  registries[ip_reg] = ip
  # print("Next instruction: " + str(registries[ip_reg]))
  next_instruction = parse_instruction(inputs[registries[ip_reg] + 1])
  run_command(next_instruction[0], next_instruction[1:3], next_instruction[3], registries)
  ip = registries[ip_reg] + 1
  # print(str(registries))
print("Final registry state: " + str(registries))