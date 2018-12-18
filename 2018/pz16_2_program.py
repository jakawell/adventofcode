import re

inputsFile = open("pz16_input.txt", "r")
inputs = inputsFile.read().split("\n\n")
print("Total inputs: " + str(len(inputs)))

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
  
def parse_registries(registry_string):
  result = []
  splits = re.split(r"\[|\]|,|\s+", registry_string)
  for reg in splits:
    if len(reg) > 0:
      result.append(int(reg))
  return result

def parse_instruction(instruction_string):
  result = []
  splits = instruction_string.split()
  for comp in splits:
    result.append(int(comp))
  return result
  
all_commands = ["addr", "addi", "mulr", "muli", 
                "banr", "bani", "borr", "bori", 
                "setr", "seti", "gtir", "gtri", 
                "gtrr", "eqir", "eqri", "eqrr"]
                
opcodes = dict()
for command in all_commands:
  opcodes[command] = list(range(16))

for example in inputs[:-2]:
  example_lines = example.split("\n")
  start_registry = parse_registries(example_lines[0].split(": ")[1])
  instruction = parse_instruction(example_lines[1])
  end_registry = parse_registries(example_lines[2].split(": ")[1])
  current_counter = 0
  for command in all_commands:
    if instruction[0] in opcodes[command] and not run_command(command, instruction[1:3], instruction[3], start_registry[:]) == end_registry:
      opcodes[command].remove(instruction[0])
  
opcode_index = 0
opcode_reference = [""] * len(all_commands)
removed = []
while opcode_index < len(opcodes):
  command = all_commands[opcode_index]
  opcode_opts = opcodes[command]
  if len(opcode_opts) == 1 and opcode_opts[0] not in removed:
    opcode_reference[opcode_opts[0]] = command
    removed.append(opcode_opts[0])
    for remove_command in all_commands:
      if remove_command != command and opcode_opts[0] in opcodes[remove_command]:
        opcodes[remove_command].remove(opcode_opts[0])
    opcode_index = 0
  else:
    opcode_index += 1

registries = [0, 0, 0, 0]
for instruction_raw in inputs[-1].split("\n"):
  instruction = parse_instruction(instruction_raw)
  run_command(opcode_reference[instruction[0]], instruction[1:3], instruction[3], registries)
print("Result registries: " + str(registries))