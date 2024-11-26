from trie import Trie

def longest_common_prefix(strs):
  
  lens = [len(str) for str in strs]
  n_strs = len(strs)
  for i in range(min(lens)):
    c = strs[0][i]
    for j in range(1, n_strs):
      if strs[j][i] != c: 
        return strs[0][:i]
  return strs[0][:min(lens)]
    
