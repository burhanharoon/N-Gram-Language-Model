# N-Gram Model Description

The Corpus for this task should be prepared by yourself. The corpus should consist of 10
different domains and each domain should have 50 distinct files. You are supposed to implement
following Python functions.

The text files are not tokenized. You need to implement a function with name _tokenize_ () that
takes the file path as its argument and returns the tokenized sentences.

Write a function _Ngram_ () that should accept two required argument, n the order of the n-gram
model & sentences and returns the n-grams.

Write a function _SentenceProb_ () that should accept a sentence and returns the probability of the
given sentence using Bigram model.

Write a function _SmoothSentenceProb_ () that should accept a sentence and returns the
probability of the given sentence using Bigram model and with Laplace smoothing.

Write a method _Perplexity_ (), that calculates the perplexity score for a given sequence of
sentences


