f = open("c:/Python-Uni/Lab-2/Class/File/Lab_12/test.txt","r")
data = f.read()

def cipher(text):
    newText = ""
    for char in text:
        # print(char)
        if char == "Z":
            c = "A"
            newText = newText + c
        elif char == "z":
            c = "a"
            newText = newText + c
        elif (65 <= ord(char) < 90) or ( 97<= ord(char) < 122):
            c = (chr(ord(char) + 1))
            newText = newText + c
        else:
            newText = newText + char
    return newText
print(cipher(data))


