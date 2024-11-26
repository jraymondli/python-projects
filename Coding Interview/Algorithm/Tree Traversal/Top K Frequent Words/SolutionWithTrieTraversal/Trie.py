from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')] is None:
                cur.children[ord(c) - ord('a')] = TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        cur.word = word

    def get_words(self, node, ans):
        if node is None:
            return
        if node.word is not None:
            ans.append(node.word)
        for i in range(26):
            if node.children[i] is not None:
                self.get_words(node.children[i], ans)
