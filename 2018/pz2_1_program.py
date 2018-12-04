inputsFile = open("pz2_input.txt", "r")
inputs = inputsFile.read().split()
print("Total inputs: " + str(len(inputs)))

twos = 0
threes = 0
for input in inputs:
  letter_counts = dict()
  for letter in input:
    if letter not in letter_counts:
      letter_counts[letter] = 1
    else:
      letter_counts[letter] = letter_counts[letter] + 1
  if 2 in letter_counts.values():
    twos += 1
  if 3 in letter_counts.values():
    threes += 1

print("Twos: " + str(twos))
print("Threes: " + str(threes))
print("Checksum: " + str(twos * threes))