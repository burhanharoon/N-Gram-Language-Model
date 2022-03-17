import re
import os
os.system('cls')


f = open("./Corpus/Entertainment/1.txt", "r")
sentence = f.read()

ab = ['Dr', 'Mr']


def split_sentences(st):
    # sentences = re.split(r"(^Dr)[.?!]\s+", st)
    # if sentences[-1]:
    #     return sentences
    # else:
    #     return sentences[:-1]
    sentence = []
    word = 'Dr'
    temp = ''
    for i in range(len(st)):
        temp += st[i]
        if st[i] == '.':
            sentence.append(temp)
            i += 1
            temp = ''
    return sentence


for sentence in split_sentences(sentence):
    print(sentence, '\n')

# print(split_sentences(sentence))
