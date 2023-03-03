word = input()
counter = 0
word_lower = word.lower()

counter += word_lower.count("fish")
counter += word_lower.count("sun")
counter += word_lower.count("sand")
counter += word_lower.count("water")

print(counter)