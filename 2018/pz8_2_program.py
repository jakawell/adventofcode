inputsFile = open("pz8_input.txt", "r")
inputs = inputsFile.read().split()
print("Total inputs: " + str(len(inputs)))

def pop_node(inputs, nodes):
  next_node = inputs[0:2]
  nodes.append([int(next_node[0]), int(next_node[1]), [0] * int(next_node[0]), 0]) # 0: child counter, 1: metadata counter, 2: child scores, 3: current child processing index
  return inputs[2:]

nodes = [[1, 0, [0], 1]] # prepopulate with parent of root

inputs = pop_node(inputs, nodes) # put the first node on the stack

while len(inputs) > 0:
  top_node = nodes[-1] # peek the top node
  if top_node[0] > 0: # top node has more children to process
    nodes[-1][0] -= 1 # decrement the parent's child count
    nodes[-1][3] += 1 # increment the parent's child index counter
    inputs = pop_node(inputs, nodes) # get the next node from the inputs
  else: # top node has no more children
    for counter in range(0, top_node[1]): # iterate over the metadata 
      metadata_value = int(inputs[0]) # get the metadata values
      if len(top_node[2]) > 0: # node had children
        if metadata_value > 0 and metadata_value <= len(top_node[2]): # if the index is valid
          nodes[-2][2][nodes[-2][3] - 1] += nodes[-1][2][metadata_value - 1] # add the child's score to the parent
      else: # node did not have children
        nodes[-2][2][nodes[-2][3] - 1] += metadata_value # add the score to the parent
      del inputs[0] # remove the metadata
    del nodes[-1] # remove the node, since we've fully processed it
    
print("The root score is " + str(nodes[0][2][0]))