from trie import Trie
from collections import defaultdict 
from heapq import heappush, heappop

class  Item:
  def __init__(self, freq, word):
    self.freq = freq 
    self.word = word 
  def __lt__(self, other):
    if self.freq == other.freq: 
      return self.word > other.word 
    else:
      return self.freq < other.freq  
      
def top_k_frequent_words(words, k):
  d = defaultdict(lambda:0)
  for w in words: d[w] += 1
  hq = []
  
  for w, f in d.items():
    heappush(hq, Item(f, w))
    if len(hq) > k: heappop(hq)
    
  result = []
  while hq:
    item = heappop(hq)
    result.append(item.word)
  result.reverse()
  return result
  
