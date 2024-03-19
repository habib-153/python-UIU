f = open("c:/Python-Uni/Lab-2/Class/File/Lab_12/output.txt","r")

data = f.read()

def cipher(text):
    newText = ""
    for char in text:
        # print(char)
        if char == "A":
            c = "Z"
            newText = newText + c
        elif char == "a":
            c = "Z"
            newText = newText + c
        elif (65 < ord(char) <= 90) or ( 97< ord(char) <= 122):
            c = (chr(ord(char) - 1))
            newText = newText + c
        else:
            newText = newText + char
    return newText
decoded_text = cipher(data)
print(decoded_text)