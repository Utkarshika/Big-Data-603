import enchant
d = enchant.Dict("en_US")
from enchant.checker import SpellChecker
chkr = SpellChecker("en_US")
file = open('file2.txt')
chkr.set_text(file)
for err in chkr:
    misspelled_words = spell.unknown(file)
    n= misspelled_words
    res = []
    for sub in n:
        res.append(sub.replace("\n", ""))
#print( str(res))
        dic = {}

        words = str(res).split()

        for raw_word in words:
             word = raw_word.lower()
             if word in dic:
                dic[word] += 1
             else:
                dic[word] = 1
                print(dic)
