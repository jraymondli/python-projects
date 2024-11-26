from trie import Trie

def find_longest_common_prefix(trie):
    prefix = ""
    node = trie.get_root()
    while node and not node.is_end_of_word and len(node.children) == 1:
        char, next_node = list(node.children.items())[0]
        prefix += char
        node = next_node
    return prefix

def longest_common_prefix(strs):
    if not strs:
        return ""

    trie = Trie()

    for word in strs:
        trie.insert(word)

    return find_longest_common_prefix(trie)
