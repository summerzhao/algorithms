#! /usr/bin/python

__author__="Stefanie Zhao <zhaochenting@gmail.com>"
__date__ ="$Mar 11, 2013"

from count_freqs import *

def calculate_counts(input):
	corpusfile = file(input,"r")
	counts = defaultdict(int)
	iterator = simple_conll_corpus_iterator(corpusfile)
	for word,tag in iterator:
		counts[word]+= 1
	return counts

def calculate_counts_test(input):
        counts = defaultdict(int)
        l = input.readline()
        while l:
                line = l.strip()
                if line: # Nonempty line
                    counts[line]+= 1                
                l = input.readline()
        return counts

def replace_rare_word(input, refined_corpusfile):
	counts = calculate_counts(input)
	corpusfile = file(input,"r")
	l = corpusfile.readline()
	while l:
                line = l.strip()
                if line: # Nonempty line
                        fields = line.split(" ")
                        ne_tag = fields[-1]
                        word = " ".join(fields[:-1])
                        if counts[word] < 5:
                                word = "_RARE_"
                        refined_corpusfile.write("%s %s\n" % (word, ne_tag))
                else: #Empty line
                        refined_corpusfile.write('\n')
                l = corpusfile.readline()


def find_max_tag(counter, word, tags):
        max_tag = ""
        max_count = 0
        for tag in tags:
              count = counter.predict_emssiion_counts[(word, tag)]
              if count > max_count:
                      max_tag = tag
                      max_count = count
        return max_tag
                

def calculate_proability(input, counter, counts, output):
        tags = set()
        for ngram in counter.ngram_counts[0]:
            ngramstr = " ".join(ngram)
            tags.add(ngramstr)

       
        rare_tag = find_max_tag(counter, "_RARE_", tags)
        
        gene_tag = find_max_tag(counter, "genes", tags)
        

        l = input.readline()
        while l:
                word = l.strip()
                if word: # Nonempty line
                        max_tag = find_max_tag(counter, word, tags)
                        if max_tag:
                               output.write("%s %s\n" % (word, max_tag))
                        else:
                                output.write("%s %s\n" % (word, rare_tag))
                else:
                        output.write("\n")
                l = input.readline()

def calulate_trigram_proability(counter, output):
        counter.trigram_prob = defaultdict(float)
        for gram_3 in counter.ngram_counts[2]:
                count_3 = counter.ngram_counts[2][gram_3]
                gram_2 = gram_3[:2]
                count_2 = counter.ngram_counts[1][gram_2]
                prob = count_3 / count_2
                counter.trigram_prob[gram_3]= prob
        for ngram in counter.trigram_prob:
                ngramstr = " ".join(ngram)
                output.write("%f %s\n" %(counter.trigram_prob[ngram], ngramstr))
                

if __name__ == "__main__":
	counter = Hmm(3)
	input = file(sys.argv[1],"r")
	counter.read_counts(input)

	#test_file = file(sys.argv[2],"r")
	#test_counts = calculate_counts_test(test_file)

	#test_file.seek(0,0)

	#calculate_proability(test_file, counter, test_counts, sys.stdout)
        calulate_trigram_proability(counter, sys.stdout)
	

	
                        
	
	
