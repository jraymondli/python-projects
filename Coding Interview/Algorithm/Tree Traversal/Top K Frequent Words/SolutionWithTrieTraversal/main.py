from collections import defaultdict
from trie import Trie


def top_k_frequent_words(words, k):
    frequency_map = defaultdict(int)
    buckets = [None] * (len(words) + 1)
    top_k = []
    
    for word in words:
        frequency_map[word] += 1

    for word, frequency in frequency_map.items():
        if buckets[frequency] is None:
            buckets[frequency] = Trie()
        buckets[frequency].add_word(word)

    for i in range(len(buckets) - 1, -1, -1):
        if buckets[i] is not None:
            retrieve_words = []
            buckets[i].get_words(buckets[i].root, retrieve_words)
            if len(retrieve_words) < k:
                top_k.extend(retrieve_words)
                k -= len(retrieve_words)
            else:
                top_k.extend(retrieve_words[:k])
                break
    return top_k

def generate_frequency_map(words):
    frequency_map = defaultdict(int)
    
    for word in words:
        frequency_map[word] += 1
    
    print("\n\tFrequency map: ")
    for key, value in frequency_map.items():
        print(f"\t{key}: {value}")

# Driver code
def main():
    words = [["apple", "banana", "orange", "banana", "banana"],
            ["cat", "dog", "fish", "bird", "cat", "dog", "fish", "bird"],
            ["python"] * 10,
            ["a", "b", "c", "a", "b", "a"],
            ["tree", "bush", "flower", "tree", "bush", "tree", "rock", "rock", "grass"]]
    
    k = [2, 4, 1, 3, 4]

    for i in range(len(words)):
        print(i + 1,".\tInput list: ", words[i])
        generate_frequency_map(words[i])
        print(f"\n\tTop {k[i]} frequent word(s):", top_k_frequent_words(words[i], k[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()
