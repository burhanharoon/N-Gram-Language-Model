import re
import os
import numpy
os.system('cls')

textFile = []
# Reads all files within the ./corpus directory and its subfolders
for path, dirs, files in os.walk('./corpus'):
    for file in files:
        read_f = open(os.path.join(path, file), 'r')
        textFile.append(read_f.read().lower())


def reverseWords(string):
    if string:
        words = string.split(' ')
        rev = ' '.join(reversed(words))
        return rev


def findCountAtStartOfSentence(word, corpus):
    count = 0
    for sentence in corpus:
        if sentence.startswith(word):
            count += 1
    return count


# Splits file into sentences
def tokenize(file):
    sentences = re.split(r"[.?!]\s+", file)
    return sentences


# Splits a sentence into words
def splitToWords(sentence):
    temp = sentence.split()
    return temp


sentences = []
for files in textFile:
    temp = (tokenize(files))
    for sentence in temp:
        sentences.append(sentence)


words = []

for sentence in sentences:
    for x in splitToWords(sentence):
        words.append(x)

totalWordsCount = len(words)
uniqueWords = set(words)
totalUniqueWordsCount = len(uniqueWords)


def getNGramString(string, ngramNumber):
    string = string.lower()
    string = splitToWords(string)
    if ngramNumber == 1:
        return string
    else:
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
                totalGrams.append(reverseWords(realWord))
        return totalGrams


def findCount(word, corpus):
    count = 0
    for sentence in corpus:
        expression = r"\b" + re.escape(word) + r"\b"
        temp = re.findall(expression, sentence)
        count += len(temp)
    return count


# returns probability of a sentence using bi-gram
def SentenceProb(sentence, corpus, totalWordsCount):
    ngramString = getNGramString(sentence, 2)
    sentence = sentence.lower().split()
    totalProbability = []
    probOfFirstWord = findCountAtStartOfSentence(
        sentence[0], corpus)/totalWordsCount
    totalProbability.append(probOfFirstWord)
    for i in range(1, len(sentence)):
        temp = findCount(ngramString[i], corpus)
        if temp:
            result = temp/findCount(sentence[i], corpus)
            totalProbability.append(result)
        else:
            totalProbability.append(0)
    result = numpy.prod(totalProbability)
    return result


# returns smooth probability of a sentence using bi-gram
def SmoothSentenceProb(sentence, corpus, totalWordsCount, uniqueWords):
    ngramString = getNGramString(sentence, 2)
    sentence = sentence.lower().split()
    totalProbability = []
    probOfFirstWord = findCountAtStartOfSentence(
        sentence[0], corpus)+1/totalWordsCount+uniqueWords
    totalProbability.append(probOfFirstWord)
    for i in range(1, len(sentence)):
        temp = (findCount(ngramString[i], corpus)+1)
        result = temp/(findCount(sentence[i], corpus)+uniqueWords)
        totalProbability.append(result)
    result = numpy.prod(totalProbability)
    return result


# Calculates perplexity of the sentence
def perplexity(probability, totalWordsCount):
    perplexity = 1/probability
    perplexity = pow(perplexity, totalWordsCount)
    return perplexity


probability = SmoothSentenceProb("The batman was a hit",
                                 sentences, totalWordsCount, totalUniqueWordsCount)

print("The probability is: ", probability)
