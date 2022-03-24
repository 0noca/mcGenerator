import random

types = [
  "block-break",
  "chat",
  "block-place",
  "craft",
  "milk",
  "smelt",
  "shear",
  "tame",
  "ride-mob",
  "regenerate",
  "move",
  "swim",
  "login",
  "kill-player",
  "kill-mob",
  "item-break",
  "gain-experience",
  "fish",
  "execute-command",
]

variables = [
  "none",
]

requiredProgress = [
  "10",
  "25",
  "50",
  "75",
  "100",
  "150",
  "250",
  "500",
  "750",
  "1000",
]

i = 8
counter = 1

def generator(types,variables,requiredProgress):
  print("  " + str(counter) + ":")
  print(str("    " + "name: " + "\'Week 1 - Quest\'"))
  print(str("    " + "type: " + types[random.randint(0,18)]))
  print(str("    " + "variable: " + variables[0])) 
  print(str("    " + "required-progress: " + requiredProgress[random.randint(0,9)]))
  print(str("    " + "points: " + "25"))
  print(str("    " + "item:"))
  print(str("      " + "material:"))
  print(str("      " + "amount: 1"))
  print(str("      " + "lore:"))
  print(str("        " + "-  " + "'" + types[random.randint(0,18)] + " " + requiredProgress[random.randint(0,9)] + " " + "times / mobs / items / meters / blocks" + "'"))
  print(str("        " + "-  " + "\''"))
  print(str("        " + "-  " + "\'%progress_bar% &7(&a%percentage_progress%&7)'"))
  

while i > 0:
  generator(types,variables,requiredProgress)
  i = i - 1
  counter = counter + 1
