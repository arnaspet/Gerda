import string
import re

search_strings = ['Legend', 'Efsane']
file_names = ['[NDS]Tomb_Raider_Legend[EUR]-[www.ESPALNDS.com].rar', '[PSP]Tomb.Raider.Legend.[EUR].rar']
hashes = ['DF8651E592919CA2D452DEC83A57FF39', 'E1760A046D8B334CB2A2F679F612F8EF']
negatives = ['ESPALNDS']

top_words = {}

for filename in file_names:
    words = re.split("[" + string.punctuation + "]+", filename)
    words = filter(lambda x: len(x) > 3, words)
    words = filter(lambda x: x not in negatives + search_strings, words)

    if words:
        print(filename + ' ' + hashes[file_names.index(filename)])

    for word in words:
        if word in top_words:
            top_words[word] += 1
        else:
            top_words[word] = 1

print(top_words)
