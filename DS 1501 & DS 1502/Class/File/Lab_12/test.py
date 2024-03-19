f = open("c:/Python-Uni/Lab-2/Class/File/Lab_12/test.txt","r")
output = open("c:/Python-Uni/Lab-2/Class/File/Lab_12/output.txt","w")
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
encoded_text = cipher(data)
print(encoded_text)
output.write(encoded_text)