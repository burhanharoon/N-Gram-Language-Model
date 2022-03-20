import re
import os
import numpy
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

testString = 'The Batman is the best'
test = 'The Batman is the best'


def getNGramString(string, ngramNumber):
    string = string.lower()
    string = splitToWords(string)
    totalGrams = [string[0]]
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
            realWord = toFindProb.strip()
            totalGrams.append(rev_words(realWord))
    return totalGrams


def findCount(word, corpus):
    count = 0
    for sentence in corpus:
        expression = r"\b" + re.escape(word) + r"\b"
        temp = re.findall(expression, sentence)
        count += len(temp)
    return count


# returns: probability of a sentence using any ngram number
# inputs: corpus, ngram number
def getTotalProbability(sentence, corpus, ngram):
    ngramString = getNGramString(sentence, ngram)
    sentence = sentence.lower()
    sentence = sentence.split()
    totalProbability = []
    totalProbability.append(findCount(sentence[0], corpus))
    for i in range(1, len(sentence)):
        temp = findCount(ngramString[i], corpus)
        if temp:
            result = temp/findCount(sentence[i], corpus)
            totalProbability.append(result)
        else:
            totalProbability.append(0)
    result = numpy.prod(totalProbability)
    return result


# returns the probability of a sentence using bigram model
def SentenceProb(sentence, corpus):
    ngramString = getNGramString(sentence, 2)
    sentence = sentence.lower()
    sentence = sentence.split()
    totalProbability = []
    totalProbability.append(findCount(sentence[0], corpus))
    for i in range(1, len(sentence)):
        temp = findCount(ngramString[i], corpus)
        if temp:
            result = temp/findCount(sentence[i], corpus)
            totalProbability.append(result)
        else:
            totalProbability.append(0)
    result = numpy.prod(totalProbability)
    return result


print(SentenceProb("The Batman", sentences))
