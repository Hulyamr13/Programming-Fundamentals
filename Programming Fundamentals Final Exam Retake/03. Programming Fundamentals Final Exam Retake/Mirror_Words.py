import re

pattern = r"([@#])([a-zA-Z]{3,})\1{2}([a-zA-Z]{3,})\1"
string = input()
pairs = re.findall(pattern, string)

if not pairs:
    print("No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")

mirror_words = {word: mirror for _, word, mirror in pairs if word == mirror[::-1]}

if mirror_words:
    print("The mirror words are:")
    words_list = [f"{word} <=> {mirror}" for word, mirror in mirror_words.items()]
    print(", ".join(words_list))
else:
    print("No mirror words!")