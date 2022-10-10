# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names_list = []
with open("Input/Names/invited_names.txt") as names:
    lines = names.readlines()
    count = 0
    for line in lines:
        count += 1
        line = line.rstrip("\n")
        names_list.append(line)
    print(names_list)

for name in names_list:
    with open("Input/Letters/starting_letter.txt") as letter:
        text = letter.read()
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        updated_text = text.replace("[name]", name)
        file.write(updated_text)
