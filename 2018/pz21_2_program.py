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
peak_4 = 0
vall_4 = 16134983

start_manual = False

while (ip + 1) < len(inputs): # next instruction is in command set
  init_4 = registries[4]
  registries[ip_reg] = ip
  pre_registries = registries[:]
  next_instruction = parse_instruction(inputs[registries[ip_reg] + 1])
  # print("Next instruction: " + str(next_instruction))
  run_command(next_instruction[0], next_instruction[1:3], next_instruction[3], registries)
  if ip == 28:
    start_manual = True
    # print("At command " + next_instruction[0] + " reg 4 is " + str(init_4))
    if first_answer < 0: # we're at the first pass through command 28, so we need to store what is in reg 4 so the equality would pass and halt the program
      first_answer = init_4
    if init_4 > peak_4:
      peak_4 = init_4
      print("New peak for register 4: " + str(init_4))
    if init_4 < vall_4:
      vall_4 = init_4
      print("New valley for register 4: " + str(init_4))
  ip = registries[ip_reg] + 1

  if start_manual:
    print("                  " + str(pre_registries))
    input("Next instruction: " + str(next_instruction) + " -->\t" + str(registries) + "  (press ENTER...)")
  
  # if registries[4] < init_4:
    # print("Register 4 decreased from " + str(init_4) + " to " + str(registries[4]))
  # if ip > 25:
  #   print("Next instruction: " + str(next_instruction))
  #   print(str(registries))
  #   print("ip = " + str(ip))
  # input("Press ENTER to continue...")
print("Final registry state: " + str(registries))
print("The lowest value for the shortest run is " + str(first_answer) + " (thanks to mamual reading of the program...)")