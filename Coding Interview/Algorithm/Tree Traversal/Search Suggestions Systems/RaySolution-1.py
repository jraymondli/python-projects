# This fails on test case 13

from trie_node import TrieNode

def addToTrie(trie, product):
  if len(product) == 0: return
  for c in product:
    if c not in trie:
      trie[c] = {}
    trie = trie[c]
  trie["product"] = product
    
def buildTrie(products):
  root = {}
  for p in products: 
    addToTrie(root, p)
  return root 
  
def annotateWithSmallest(trie):
  p_list = []
  if "product" in trie: 
    p_list.append(trie["product"])
  for k, sub_trie in trie.items():
    if k != "product": 
      p_list.extend(annotateWithSmallest(sub_trie))
  p_list.sort()
  p_list = p_list[:3]
  trie["suggestions"] = p_list
  return p_list
  
def searchTrie(trie, word):
  for c in word:
    if c not in trie: 
      return []
    trie = trie[c]
  return trie["suggestions"]
  
def suggested_products(products, search_word):

    trie = buildTrie(products)
    annotateWithSmallest(trie)
    print(trie)
    results = []
    for i in range(len(search_word)):
      result = searchTrie(trie, search_word[:i+1])
      results.append(result)
    return results
