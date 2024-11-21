def reverse_words(sentence):

  ns = len(sentence)
  r_array = []
  s, e = ns-1, ns
  for s in range(ns-1, -1, -1):
    if sentence[s] != ' ':
      s -= 1 
    else: 
      w = sentence[s+1:e]
      if w not in ['', ' ']:
        r_array.append(w)
      e = s 
      
  w = sentence[0:e]
  if w not in ['', ' ']:
        r_array.append(w)
  return ' '.join(r_array)
