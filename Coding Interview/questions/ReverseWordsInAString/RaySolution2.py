def reverse_str(str):
  rv = ""
  for c in str:
    rv = c + rv 
  return rv 
  
def reverse_words(sentence):
  sentence = sentence.rstrip()
  sentence = reverse_str(sentence)
  sentence = sentence.rstrip() 
  
  ls = len(sentence)
  s = e = 0 
  r_array = []
  for e in range(ls):
    if sentence[e] == ' ':
      word = sentence[s:e]
      if word not in ['', ' ']:
        r_array.append(reverse_str(word))
      s = e+1 
  word = sentence[s:e+1]
  if word not in ['', ' ']:
      r_array.append(reverse_str(word))
  return ' '.join(r_array)
