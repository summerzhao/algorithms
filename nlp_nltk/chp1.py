from __future__ import division
__author__ = 'stefanie'

from nltk.book import *

word = "monstrous"

#basic operation on text which is a word-list
print("the length of text1")
print len(text1)
print("the last word in text1 based on sorting by alpha")
print sorted(set(text1))[-1]
print("the average frequent of word in text1")
print len(text1)/len(set(text1))
print("how many 'very' in text1")
print text1.count("very")

#basic on word and word-context index
print("show the concordance of word monstrous")
text1.concordance(word)
print("show the similar word of monstrous")
text1.similar(word)
print("show the common context of two words")
text2.common_contexts(["monstrous", "very"])

print("show the distribution map of words")
text4.dispersion_plot(["citizen","democracy","freedom","duties","America"])

#will build a n-gram index
print("random generate sample text")
text3.generate()

print("show the word frequent in text1")
fdist1 = FreqDist(text1)
print(len(fdist1.keys()))  # is equals to len(set(text1))
print("show the frequent of whale")
print fdist1["whale"]
print("show the frequent plot of first 50 words")
fdist1.plot(50, cumulative=True)
print("how many words only occur once")
print len(fdist1.hapaxes())
print("find the frequency diagram of word length in text1")
fdist_wl = FreqDist(len(w) for w in text1)
print fdist_wl.keys()
print "the most frequent word length"
print fdist_wl.max()
print "the frequent of most frequent word"
print fdist_wl.freq(fdist_wl.max())

#bigrams and n-gram
sample = ['more','is','said','than','done']
print("generate bigrams")
bigrams(sample)
#will build collocation list
print("find the most frequent bi-gram in text1")
text1.collocations()







