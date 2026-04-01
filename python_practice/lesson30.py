import os
# f = open("demofile.txt", "rt")
# print(f.read())
# f.close()

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt", "r") as f:
  print(f.read())
  f.close()

  #x = write / a = append / r = read / w = write (overwrites the file)
  if os.path.exists("mytext.txt"):
    # f = open("mytext.txt","rt")
    # print(f.read())
    # f.close()
    os.remove("mytext.txt") #removes the file
    # os.rmdir("myfolder") #removes the folder
  else:
    f = open("mytext.txt","x")
    f.write("Hello World!")
    print(f.readline())
    f.close()