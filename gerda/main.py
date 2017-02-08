import string
import re
import csv
import operator
import sys


search_strings = []
file_names = []
hashes = []
negatives = []

result_file = open('result.csv', 'w')
top_words_file = open('top_words.csv', 'w')
result_file_writer = csv.writer(result_file)
top_words_writer = csv.writer(top_words_file)

with open(sys.argv[1], 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        hashes.append(row[0])
        file_names.append(row[1])
        if row[2] != '':
            search_strings.append(row[2])

with open('ignore.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        negatives.append(row[0])


top_words = {}

for filename in file_names:
    words = re.split("[" + string.punctuation + "]+", filename)
    words = filter(lambda x: len(x) > 3, words)
    words = filter(lambda x: x not in negatives + search_strings, words)

    if words:
        result_file_writer.writerow([filename + ' ' + hashes[file_names.index(filename)]])

    for word in words:
        if word in top_words:
            top_words[word] += 1
        else:
            top_words[word] = 1

sorted_top_words = sorted(top_words.items(), key=operator.itemgetter(1), reverse=True)
top_words_writer.writerows(sorted_top_words)
