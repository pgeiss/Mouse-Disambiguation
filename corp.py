import os
import nltk
import pickle
import zlib
import base64
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.classify import PositiveNaiveBayesClassifier
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

corpusdir = './text'
newcorpus = PlaintextCorpusReader(corpusdir, '.*')
labeled_names = ([(name, 'comp') for name in newcorpus.words('comp.txt')] + \
	[(name, 'animal') for name in newcorpus.words('animal.txt')] + \
	[(word, 'ignore') for word in newcorpus.words('ignorethese.txt')])
features = [({n:n}, thing) for (n, thing) in labeled_names]
training = features[:]
testing = 'What color is the mouse?'.lower().split(' ')
classifier = NaiveBayesClassifier.train(training)
pickleclf=pickle.dumps(classifier)
compressed = base64.b64encode(zlib.compress(pickleclf,9))
with open("PickledClassifier.txt","wb") as outobj:
     outobj.write(compressed)
compScore = 0
animalScore = 0
for word in testing:
	if (word[len(word) - 1] == '.' or word[len(word) - 1] == ',' 
		or word[len(word) - 1] == '?' or word[len(word) - 1] == '!'):
		word = word[:len(word) - 1]
	result = classifier.classify({word:word})
	if (result == 'comp'):
		compScore += 1
		print word
	elif (result == 'animal'):
		animalScore += 1
print compScore
print animalScore
print len(testing) - compScore - animalScore