    # with open('file.txt') as f:
    #     contents = f.read(10)
    #     print(contents)

f = open("file.txt", "+a")
# print(f.read())

# Reading Line by Line
# for line in f:
    # print(line)     ............... print(line.strip()) -- for preventing to print extra line

cont= ''
line = f.readlines()
# print(line)
for l in line:
    cont=cont+l.strip()
# print(cont)
# print(len(cont))
    
f.write("You Can't")

# ===============
"""
Read = "r"
write = "w"
do not remove previous text/ append on file = "a"
read and append = "+a"
read and write = "+w"

"""