Alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z')

alphabet_count = dict()

with open("input_ex5.txt", "r") as file:
    text_value = file.read().lower()

for i in range(26):
    alphabet_count[Alphabet[i]] = text_value.count(Alphabet[i])

sorted_alphabet_count = dict()
sorted_keys = sorted(alphabet_count, key=alphabet_count.get, reverse=True)

with open("output_ex5.txt", "w") as file:
    for key in sorted_keys:
        file.write(str(key) + " " + str(alphabet_count[key]) + "\n")
