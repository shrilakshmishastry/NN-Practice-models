# program to create csv file for a given txt file


import csv
from om_transliterator import Transliterator
from polyglot.transliteration import Transliterator


with open('words.txt','r') as in_file:

    stripped = (line.strip() for line in in_file)
    # for k in stripped:
    #     print(k)
    # print(type(k))
    lines = (line.split("\t") for line in stripped if lines)
    # print(type(lines))

    with open ('words.csv','w') as out_file:
        write= csv.writer(out_file)
        write.writerow(('number','kannada_word','english'))
        write.writerow(lines)
        out_file.close()

kannada_words = []
with open('words.csv','r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    next(csvreader)

    for k in csvreader:
        for i in range(0,len(k)):
            word = k[i].strip('][').split(',')[1]
            # print(word.replace('\'',''))
            kannada_words.append(word.replace('\'',' '))
    csvfile.close()


# print(kannada_words[0])


transliterator = Transliterator()
# print(transliterator.knda_to_latn(kannada_words[0]))

word_set=[]
# word_set1 = []
# for words in kannada_words:
#     print(words+",")
#     traslited_text = ""
#     traslited_text = transliterator.knda_to_latn(words)
#     print(traslited_text)
#     word_set.append(traslited_text)
# print(word_set)
for k in kannada_words:
    # print(k)
    # transliterator.knda_to_latn(" ")

    word = transliterator.knda_to_latn(k).strip(" ").split()

word_set1 = word
# print()
# print(word_set1)
for i in word_set1:
    print(i)
