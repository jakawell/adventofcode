inputsFile = open("pz8_input.txt", "r")
inputs = inputsFile.read().split()
print("Total inputs: " + str(len(inputs)))

def pop_node(inputs, nodes):
  next_node = inputs[0:2]
  nodes.append([int(next_node[0]), int(next_node[1])])
  return inputs[2:]

nodes = []
metadata_total = 0

inputs = pop_node(inputs, nodes) # put the first node on the stack

while len(inputs) > 0:
  top_node = nodes[-1] # peek the top node
  if top_node[0] > 0: # top node has more children to process
    nodes[-1][0] -= 1 # decrement the parent's child count
    inputs = pop_node(inputs, nodes) # get the next node from the inputs
  else: # top node has no more children
    for counter in range(0, top_node[1]): # iterate over the following metadata
      metadata_total += int(inputs[0]) # add the metadata
      del inputs[0] # remove the metadata
    del nodes[-1] # remove the node, since we've fully processed it
    
print("Total metadata: " + str(metadata_total))