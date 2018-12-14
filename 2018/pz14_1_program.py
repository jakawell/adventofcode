inputsFile = open("pz14_input.txt", "r")
recipe_max = int(inputsFile.read())
print("The max recipe count is " + str(recipe_max))

recipes = [3, 7]
elf_1_index = 0
elf_2_index = 1

def print_recipes(recipes, elf_1_index, elf_2_index):
  for recipe in range(len(recipes)):
    if recipe == elf_1_index:
      print("(" + str(recipes[recipe]) + ")", end="")
    elif recipe == elf_2_index:
      print("[" + str(recipes[recipe]) + "]", end="")
    else:
      print(" " + str(recipes[recipe]) + " ", end="")
  print()

while len(recipes) <= recipe_max + 10:
  new_total = recipes[elf_1_index] + recipes[elf_2_index]
  if new_total > 9:
    recipes.append(int(new_total / 10))
    recipes.append(new_total % 10)
  else:
    recipes.append(new_total)
    
  elf_1_index = (elf_1_index + recipes[elf_1_index] + 1) % len(recipes)
  elf_2_index = (elf_2_index + recipes[elf_2_index] + 1) % len(recipes)
  
final_recipes = ""
for recipe in range(recipe_max, recipe_max + 10):
  final_recipes += str(recipes[recipe])
print("Final 10 recipes: " + final_recipes)