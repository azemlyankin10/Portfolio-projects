import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
str = 'Andrii'
# rows = [row['code'] for (index, row) in data.iterrows() if row['letter'].lower() in str.lower()]
# print(rows)

# res = []
#
# for letter in str:
#     letter = letter.lower()
#     for (index, row) in data.iterrows():
#         if row['letter'].lower() == letter:
#             res.append(row['code'])
#             break

# print(res)

dict = {row['letter'].lower(): row['code'] for (index, row) in data.iterrows()}
res = [dict[letter] for letter in str.lower()]
print(res)