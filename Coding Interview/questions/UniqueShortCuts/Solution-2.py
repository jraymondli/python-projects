def build_set(word):
    c_set = set()
    for c in word:
        c_set.add(c)
    return c_set

def build_char_sets(text):
    dicts = []
    for word in text:
        d = build_set(word)
        dicts.append(d)
    return dicts


def findShortestSub(text, i, dicts):
    nw = len(text)
    word = text[i]
    wl = len(word)
    for sl in range(1, wl):
        for idx in range(0, wl-sl+1):
            ss = word[idx:idx+sl]
            found_match = False
            for j in range(nw):
                if j == i: continue 
                if ss in dicts[j]:
                    found_match = True 
                    break 
            if not found_match:
                return idx, sl 

def find_shortest(text):
    nw = len(text)
    dicts = build_char_sets(text)
    print(dicts)

    results = []
    for i in range(nw):
        word = text[i]
        idx, s_len = findShortestSub(text, i, dicts)
        new_word = word[:idx] + "<u>" + word[idx:idx + s_len] + "</u>" + word[idx + s_len:]
        results.append(new_word)

    return results


text = ["abc", "aef", "cby"]
print(find_shortest(text))
