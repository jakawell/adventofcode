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

behave_like_count = 0
for example in inputs[:-2]:
  example_lines = example.split("\n")
  start_registry = parse_registries(example_lines[0].split(": ")[1])
  instruction = parse_instruction(example_lines[1])
  end_registry = parse_registries(example_lines[2].split(": ")[1])
  current_counter = 0
  for command in all_commands:
    if run_command(command, instruction[1:3], instruction[3], start_registry[:]) == end_registry:
      current_counter += 1
  if current_counter >= 3:
    behave_like_count += 1
print(str(behave_like_count) + " samples behave like three or more opcodes.")