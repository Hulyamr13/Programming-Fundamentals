import re

text = input()

# Compile the regular expression pattern for finding valid emojis
emoji_pattern = re.compile(r"(:{2}|\*{2})([A-Z][a-z]{2,})\1")

# Find all valid emojis in the text using the compiled pattern
emojis = emoji_pattern.findall(text)

# Calculate the cool threshold by multiplying all digits in the input
cool_threshold = 1
for c in text:
    if c.isdigit():
        cool_threshold *= int(c)

# Initialize lists for all emojis and cool emojis
all_emojis = []
cool_emojis = []

# Check if each emoji is cool and add it to the appropriate list
for emoji in emojis:
    # Calculate the sum of ASCII values for the word in the emoji
    ascii_sum = sum(ord(c) for c in emoji[1])

    # Check if the emoji is cool and add it to the appropriate list
    if ascii_sum >= cool_threshold:
        cool_emojis.append(emoji[0] + emoji[1] + emoji[0])
    all_emojis.append(emoji[0] + emoji[1] + emoji[0])

# Print the results
print(f"Cool threshold: {cool_threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)