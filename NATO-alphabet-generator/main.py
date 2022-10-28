import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

is_on = True
while is_on:
    name = input("Please enter your name? \n").upper()
    try:
        name_list = [data_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, Only letters in the Alphabet please")
        is_on = True
    else:
        print(name_list)
        is_on = False
