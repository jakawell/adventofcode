inputsFile = open("pz21_input.txt", "r")
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
registries = [0, 0, 0, 0, 0, 0]

first_answer = -1
start_manual = False

while (ip + 1) < len(inputs): # next instruction is in command set
  init_4 = registries[4]
  registries[ip_reg] = ip
  pre_registries = registries[:]
  next_instruction = parse_instruction(inputs[registries[ip_reg] + 1])
  run_command(next_instruction[0], next_instruction[1:3], next_instruction[3], registries)
  if ip == 28:
    start_manual = True
    if first_answer < 0: # we're at the first pass through command 28, so we need to store what is in reg 4 so the equality would pass and halt the program
      first_answer = init_4
      break
  ip = registries[ip_reg] + 1
print("Final registry state: " + str(registries))
print("The lowest value for the shortest run is " + str(first_answer) + " (thanks to mamual reading of the program...)")