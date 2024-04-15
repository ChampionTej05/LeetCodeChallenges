# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.indexes = []

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word, index):
#         node = self.root
#         node.indexes.append(index)  # Store the word index at the root node
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#             node.indexes.append(index)
    
#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 return []  # No such word exists
#             node = node.children[char]
#         return node.indexes

# class WordFilter:
#     def __init__(self, words):
#         self.prefixTrie = Trie()
#         self.suffixTrie = Trie()
#         for index, word in enumerate(words):
#             self.prefixTrie.insert(word, index)
#             self.suffixTrie.insert(word[::-1], index)
    
#     def f(self, pref, suff):
#         prefixMatches = self.prefixTrie.search(pref)[::-1]
#         suffixMatches = self.suffixTrie.search(suff[::-1])[::-1]

#         # Find the highest index present in both lists
#         i = j = 0
#         while i < len(prefixMatches) and j < len(suffixMatches):
#             if prefixMatches[i] == suffixMatches[j]:
#                 return prefixMatches[i]  # Found a matching index
#             elif prefixMatches[i] > suffixMatches[j]:
#                 i += 1
#             else:
#                 j += 1
#         return -1  # No matching word found
    


## Simple Trie Implementation 
from collections import defaultdict
def Trie():
    return defaultdict(Trie)

# guaranteed to be unique if a & b are only lowercase letters 
def hash_for_lowercase(a,b):
    return ord(a)*128 + ord(b)
    
root = Trie()
words = ["abcd", "abd", "abdeabd"]
special_char = '*' # this is used in each node of trie, to tell what is the count of words matched at this index 
#  since this is not from lower case english letters, it is always guaranteed to not conflict with existing character and trie nodes 
special_char_default_count = 0
answer = 0 #storing how many match prefix and suffix 
for word in words:
    current = root
    for chr in zip(word, reversed(word)):
        node = hash_for_lowercase(chr[0],chr[1])
        if node not in current:
            current[node] = Trie()
        # go to it's child in the tree
        current = current[node]
        # check how many words were matched on this node previously. 0 if none were matched 
        answer += current.get(special_char, special_char_default_count)
    #word is ended so now mark this as count=1 or whatever is existing + 1
    current[special_char] = current.get(special_char,special_char_default_count) + 1
   
print("Answer : ", answer) 

#same question can be done using hashing to store integer has for faster computation  
# here we store (prefix+suffix) in dictionary_key 
# instead we can store hash(prefix,suffix) for faster computation 



        



