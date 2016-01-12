import os
import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.classify import PositiveNaiveBayesClassifier
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

def features(sentence):
	words = sentence.lower().split()
	return dict(('contains(%s)' % w, True) for w in words)

corpusdir = './text'
newcorpus = PlaintextCorpusReader(corpusdir, '.*')
positive_featuresets = list(map(features, newcorpus.raw('comp.txt')))
unlabeled_featuresets = list(map(features, newcorpus.raw('animal.txt')))
classifier = PositiveNaiveBayesClassifier.train(positive_featuresets, 
	unlabeled_featuresets, .3)
print classifier.classify(features('.'))