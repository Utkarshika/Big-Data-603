# !pip install pyspellchecker
# !pip install pandas

import pandas as pd
from spellchecker import SpellChecker


spell = SpellChecker()
# file = open('file2.txt')
file = pd.read_csv('file2.txt', encoding='latin-1',  on_bad_lines='skip')

non_english_words = spell.unknown(file)
result = []
for word in non_english_words:
    result.append(word.replace("\n", ""))
dict_words = {}

words = str(result).split()

for sample_words in words:
    word = sample_words.lower()
    if word in dict_words:
        dict_words[word] += 1
    else:
        dict_words[word] = 1
print(dict_words)
