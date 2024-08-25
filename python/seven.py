# f = open("demo.txt","r")
# data = f.read()
# print(data)
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)
# print(type(data))
# f.close()

# f = open("demo.txt", "r+")
# f.write("my name is nikhil what is your")
# f.close

# with open("demo.txt", "r") as f:
#  data = f.read()
#  print(data)

# with open("demo.txt", "w") as f:
#   f.write("my namee is iron man")

# import os
# os.remove("sample.txt")

# with open("demo.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nUsing java.\ni like programming in java")


with open("demo.txt", "r") as f:
    data = f.read()
   
new_data = data.replace("java", "python")
print(new_data.find("learning"))
