import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {}
for (index, row) in data.iterrows():
    row_letter = row.letter
    row_code = row.code
    data_dict.update({row_letter: row_code})

name = input("Please enter your name? \n").upper()

name_list = [data_dict[letter] for letter in name]
print(name_list)
