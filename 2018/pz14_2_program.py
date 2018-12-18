inputsFile = open("pz14_input.txt", "r")
recipe_to_find = inputsFile.read()
print("The recipe to find is " + recipe_to_find)

recipes = "37"
elf_1_index = 0
elf_2_index = 1
found_index = None

def print_recipes(recipes, elf_1_index, elf_2_index):
  for recipe in range(len(recipes)):
    if recipe == elf_1_index:
      print("(" + str(recipes[recipe]) + ")", end="")
    elif recipe == elf_2_index:
      print("[" + str(recipes[recipe]) + "]", end="")
    else:
      print(" " + str(recipes[recipe]) + " ", end="")
  print()

while found_index is None:
  new_total = int(recipes[elf_1_index]) + int(recipes[elf_2_index])
  if new_total > 9:
    recipes += (str(int(new_total / 10)))
    recipes += (str(new_total % 10))
  else:
    recipes += (str(new_total))
    
  elf_1_index = (elf_1_index + int(recipes[elf_1_index]) + 1) % len(recipes)
  elf_2_index = (elf_2_index + int(recipes[elf_2_index]) + 1) % len(recipes)
  
  if recipes.endswith(recipe_to_find):
    found_index = len(recipes) - len(recipe_to_find)
    
  #print_recipes(recipes, elf_1_index, elf_2_index)
  
print("Recipe found after " + str(found_index) + " recipes.")