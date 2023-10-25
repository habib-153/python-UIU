num_to_words = {1:'One', 2:'Two', 3:'Three', 4:'Four'}

for key, value in num_to_words.items():
    print(key, value)

print(num_to_words.keys())
print(num_to_words.values())
print(num_to_words[3])
print(num_to_words.get(4))  
print(num_to_words.items())       

# print(dir(num_to_words))