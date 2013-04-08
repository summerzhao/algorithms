#! /usr/bin/python
from __future__ import division
__author__="Alexander Rush <srush@csail.mit.edu>"
__date__ ="$Sep 12, 2012"

import sys, json

"""
Count rule frequencies in a binarized CFG.
"""

class Counts:
  def __init__(self):
    self.unary = {}
    self.binary = {}
    self.nonterm = {}
    self.unary_pob = {}
    self.unary_pob_reorg = {}
    self.binary_pob = {}
    self.binary_pob_reorg = {}

  def show(self):
    for symbol, count in self.nonterm.iteritems():
      print count, "NONTERMINAL", symbol

    for (sym, word), count in self.unary.iteritems():
      print count, "UNARYRULE", sym, word

    for (sym, y1, y2), count in self.binary.iteritems():
      print count, "BINARYRULE", sym, y1, y2

    if len(self.unary_pob)>0:
      for (sym, word), freq in self.unary_pob.iteritems():
        print freq, "UNARYRULE_FREQ", sym, word

    if len(self.binary_pob)>0:
      for (sym, y1, y2), freq in self.binary_pob.iteritems():
        print freq, "BINARYRULE_FREQ", sym, y1, y2
      
  def load(self, input):
    for l in input:
      parts = l.strip().split(" ")
      count = float(parts[0])
      if parts[1] == "NONTERMINAL":
        symbol = parts[2]
        self.nonterm[symbol] = count
      elif parts[1].endswith("UNARYRULE"):
        symbol = parts[2]
        word = parts[3]
        self.unary[(symbol, word)] = count
      elif parts[1] == "BINARYRULE":
        symbol = parts[2]
        y1 = parts[3]
        y2 = parts[4]
        self.binary[(symbol, y1, y2)] = count
      elif parts[1] == "UNARYRULE_FREQ":
        symbol = parts[2]
        word = parts[3]
        self.unary_pob[(symbol, word)] = count
        if not self.unary_pob_reorg.has_key(word):
          self.unary_pob_reorg[word] = {}
        self.unary_pob_reorg[word][symbol] = count 
      elif parts[1] == "BINARYRULE_FREQ":
        symbol = parts[2]
        y1 = parts[3]
        y2 = parts[4]
        self.binary_pob[(symbol, y1, y2)] = count
        if not self.binary_pob_reorg.has_key(symbol):
          self.binary_pob_reorg[symbol] = {}
        self.binary_pob_reorg[symbol][(y1,y2)] = count

  def estimate(self):
    for (sym, word), count in self.unary.iteritems():
      self.unary_pob[(sym, word)] = count / self.nonterm[sym]
    for (sym, y1, y2), count in self.binary.iteritems():
      self.binary_pob[(sym, y1, y2)] = count / self.nonterm[sym]

  def count(self, tree):
    """
    Count the frequencies of non-terminals and rules in the tree.
    """
    if isinstance(tree, basestring): return

    # Count the non-terminal symbol. 
    symbol = tree[0]
    self.nonterm.setdefault(symbol, 0)
    self.nonterm[symbol] += 1
    
    if len(tree) == 3:
      # It is a binary rule.
      y1, y2 = (tree[1][0], tree[2][0])
      key = (symbol, y1, y2)
      self.binary.setdefault(key, 0)
      self.binary[(symbol, y1, y2)] += 1
      
      # Recursively count the children.
      self.count(tree[1])
      self.count(tree[2])
    elif len(tree) == 2:
      # It is a unary rule.
      y1 = tree[1]
      key = (symbol, y1)
      self.unary.setdefault(key, 0)
      self.unary[key] += 1

def main(parse_file):
  counter = Counts() 
  for l in open(parse_file):
    t = json.loads(l)
    counter.count(t)
  #counter.show()
  #counter.load(open(parse_file))
  counter.estimate()
  counter.show()

def usage():
    sys.stderr.write("""
    Usage: python count_cfg_freq.py [tree_file]
        Print the counts of a corpus of trees.\n""")

if __name__ == "__main__": 
  if len(sys.argv) != 2:
    usage()
    sys.exit(1)
  main(sys.argv[1])
  
