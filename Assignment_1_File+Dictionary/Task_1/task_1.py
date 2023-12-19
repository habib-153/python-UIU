f = open("c:\Python-Uni\Lab-2\Assignment_1_File+Dictionary\Task_1/statements.txt")
info = f.readlines()
# print(info)
name = ""
suspects = {}
lst = ["At home", "On a business trip", "At the library"]
for i in info:
    # print(i.strip())
    i = i.strip()
    if i == "-":
        continue
    elif i.isalpha():
        name = i
        suspects[name] = {"alibi": "", "behavior": ""}
    elif any(x in i for x in lst):
        suspects[name]["alibi"] = i
    else:
        suspects[name]["behavior"] = i

# print(suspects)
culprit = ""
for key,value in suspects.items():
    if "arguing with the museum curator" in value["behavior"]:
        culprit = key
        break

w = open("c:\Python-Uni\Lab-2\Assignment_1_File+Dictionary\Task_1/culprit.txt", "w")
w.write(f"{culprit} is the culprit because {suspects[culprit]['behavior']}")