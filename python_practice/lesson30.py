# f = open("demofile.txt", "rt")
# print(f.read())
# f.close()

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt", "r") as f:
  print(f.read())