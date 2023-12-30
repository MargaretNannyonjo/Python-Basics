with open("maggie.txt", "w") as file:
   file.write("This is line 1\n")
   file.write("This is line 2\n")
   file.write("This is line 3\n")
   file.write("This is line 4\n")
   file.write("This is line 5\n")
   print("Content Updated")

with open("maggie.txt", "r") as file:
   content = file.read()
   print(content)
