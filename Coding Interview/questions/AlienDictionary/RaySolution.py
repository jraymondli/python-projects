from collections import defaultdict, Counter, deque

def getPerPairOrder(word1, word2):
  nw = min(len(word1), len(word2))
  for i in range(nw):
    if word1[i] == word2[i]: continue 
    return [word1[i], word2[i]]
  if len(word1) > len(word2): return [-1, -1]
  return []
  
def getOrders(words):
  results = [] 
  for i in range(len(words) -1):
    order = getPerPairOrder(words[i], words[i+1])
    if order: results.append(order)
  return results
  
def alien_order(words):

    orders = getOrders(words)
    print("orders:",orders)
    d_dict, p_dict = defaultdict(lambda:[]), defaultdict(lambda:[])
    for c1, c2 in orders:
      if c1 == -1: return ""
      d_dict[c1].append(c2)
      p_dict[c2].append(c1)
    c_set = set()
    all_c = set()
    dq = deque()
    for word in words:
      for c in word:
        all_c.add(c)
        if len(p_dict[c]) == 0: c_set.add(c)
    for c in c_set: dq.append(c)
    result = []
    while dq:
      c = dq.popleft() 
      result.append(c)
      # print(result)
      for nxt in d_dict[c]:
        if c in p_dict[nxt]: p_dict[nxt].remove(c)
        if p_dict[nxt] == []: dq.append(nxt)
    if len(result) != len(all_c): return ""
    print(dq)
    return "".join(result)
