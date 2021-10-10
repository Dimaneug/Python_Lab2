import string

with open("input_1.txt", "r") as file:
    text1 = list(filter(None, (word.strip(string.punctuation) for word in file.read().lower().split())))

with open("input_2.txt", "r") as file:
    text2 = list(filter(None, (word.strip(string.punctuation) for word in file.read().lower().split())))

same_words = ""

for word1 in text1:
    if word1 in same_words:
        continue
    for word2 in text2:
        if word1 == word2:
            same_words += word1 + " "
            break

with open("output_ex4.txt", "w") as file:
    file.write(same_words)
