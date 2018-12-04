inputsFile = open("pz2_input.txt", "r")
inputs = inputsFile.read().split()
print("Total inputs: " + str(len(inputs)))

def compare_ids(id1, id2):
  differences = 0
  cleaned_id = ""
  for index in range(0, len(id1)):
    if id1[index] != id2[index]:
      differences += 1
    else:
      cleaned_id += id1[index]
    if differences > 1:
      return None
  return cleaned_id

checked_inputs = []
for input in inputs:
  for checked_input in checked_inputs:
    id_comparison = compare_ids(input, checked_input)
    if id_comparison is not None:
      print("Found matches! " + input + " and " + checked_input)
      print("Cleaned id:    " + id_comparison)
  checked_inputs.append(input)