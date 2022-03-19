import re
import os
os.system('cls')

f = open("./Corpus/Entertainment/1.txt", "r")
textFile = f.read().lower()


def rev_words(string):
    if string:
        words = string.split(' ')
        rev = ' '.join(reversed(words))
        return rev


# Splits file into sentences
def splitToSentences(st):
    sentences = re.split(r"[.?!]\s+", st)
    return sentences


# Splits a sentence into words
def splitToWords(sentence):
    temp = sentence.split()
    return temp


sentences = splitToSentences(textFile)

words = []

for sentence in sentences:
    for x in splitToWords(sentence):
        words.append(x)

wordTypes = {}

for word in words:
    if word in wordTypes:
        wordTypes[word] += 1
    else:
        wordTypes[word] = 1


def getNGramString(string, ngramNumber):
    string = string.lower()
    string = splitToWords(string)
    totalGrams = []
    for index, word in enumerate(string):
        i = index
        toFindProb = ''
        if index > 0 and ngramNumber > 1:
            for j in range(ngramNumber):
                if i >= 0:
                    toFindProb = toFindProb + string[i]
                    toFindProb += ' '
                    i -= 1
        if toFindProb:
            totalGrams.append(rev_words(toFindProb))
    return totalGrams


test = 'The Batman is the best'
print(getNGramString(test, 4))
