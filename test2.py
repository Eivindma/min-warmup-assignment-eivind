

lines = ["det var En Gang", "Legenden er her"]
word_list = []
for line in lines:
    
    words = line.split()
    for word in words:
        word = word.lower().strip()
        word_list.append(word)
        

print(word_list)