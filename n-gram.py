import re
import os
os.system('cls')


f = open("./Corpus/Entertainment/1.txt", "r")
textFile = f.read()

ab = ['Dr', 'Mr']


# Splits the file into sentences
def splitToSentences(st):
    sentences = re.split(r"[.?!]\s+", st)
    return sentences


# Splits the sentence into words
def splitToWords(sentence):
    temp = sentence.split()
    return temp


# def sentenceProbability(sentence):
sentences = splitToSentences(textFile)

words = []

for sentence in sentences:
    for x in splitToWords(sentence):
        words.append(x)

wordTypes = {}

for word in words:
    lowerWord = word.lower()
    if lowerWord in wordTypes:
        wordTypes[lowerWord] += 1
    else:
        wordTypes[lowerWord] = 1


# Calculates Bigram
temp = 'matt reeves directed the batman'
