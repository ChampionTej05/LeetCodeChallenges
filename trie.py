'''
Classic Implementation of Trie 

Trie is N-ary tree with root having more than one children 
Leaf nodes are special nodes which marks the end of the word or every node can have flag to denote if it is last node of the word

insert -> Inserts a word in trie data structure 
'''


class TrieNode:

    def __init__(self, value):
        self.value = value
        #  holds the childrens for that node
        self.children = {}
        self.is_leaf_node = False

    # def __repr__(self) -> str:
    #     print(self.value)
        
    def __repr__(self) -> str:
        return self.value if self.value else "EMPTY_ROOT"

class Trie:

    def __init__(self):
        self.root = TrieNode(None)
        
    def __repr__(self) -> str:
        from collections import deque
        queue = deque()

        node = self.root 
        queue.append(node)
        result = "Trie:\n"

        while queue:
            queue_length = len(queue)
            level_nodes = []

            for i in range(queue_length):
                node = queue.popleft()
                if node.value is not None:
                    level_nodes.append(node.value)

                # Enqueue all children of the current node
                for child in node.children.values():
                    queue.append(child)

            if level_nodes:
                result += " ".join(level_nodes) + "\n"

        return result
               


    def insert(self, word):
        print("Word to be inserted : ", word)
        node = self.root
        # print("Word Workign ", word)
        for character in word:
            # print("character : ", character)
            if character not in node.children:
                node.children[character] = TrieNode(character)    
            node = node.children[character]
                

            # print("node : {}".format(node.children))
        node.is_leaf_node = True
        

    def startsWith(self, word):
        node = self.root 

        for character in word:
            if character not in node.children:
                return False 
            node = node.children[character]

        return True  
    
    def search(self, prefix):
        
        node = self.root 

        for character in prefix:
            if character not in node.children:
                return False 
            node = node.children[character]

        if node.is_leaf_node:
            return True 
        return False





instructions = ["Trie","insert","insert", "insert","insert", "search", "search", "startsWith", "insert", "search"]
data = [[], ["apple"], ["aplet"], ["remark"] ,["remarking"],["aplet"],["app"], ["app"], ["app"], ["an"]]


# instructions = ["WordFilter", "f"]
# # data = [[["apple"]], ["a", "e"]]
# data = [[["abbba", "abba"]], ["ab", "ba"]]

trie = Trie()
reverse_trie = Trie()
for idx in range(len(instructions)):
    instruction = instructions[idx]
    
    if instruction == 'insert':
        trie.insert(data[idx][0])

    elif instruction == "search":
        result = trie.search(data[idx][0])
        print("Request : {} , Search Result : {}".format(data[idx][0], result))

    elif instruction == "startsWith":
        result = trie.startsWith(data[idx][0])
        print("Request : {} , startsWith Result : {}".format(data[idx][0], result))


# max_idx = -1
# for idx in range(len(instructions)):
#     instruction = instructions[idx]
    
#     if instruction == 'WordFilter':
#         words = data[idx][0]
#         for word in words:
#             trie.insert(word)
#             reverse_trie.insert(word[::-1])

#     elif instruction == "search":
#         result = trie.search(data[idx][0])
#         print("Request : {} , Search Result : {}".format(data[idx][0], result))

#     elif instruction == "f":
#         prefix, suffix = data[idx]
#         print("Prefix to be searched: {}, suffix : {}".format(prefix, suffix[::-1]))
#         prefix_found = trie.startsWith(prefix)
#         suffix_found = reverse_trie.startsWith(suffix[::-1])
#         if prefix_found and suffix_found:
#             max_idx = max(idx, max_idx)
#         print("Request : {} , startsWith Result : {}".format(data[idx],  prefix_found and suffix_found))


# print(max_idx)


# print(trie)
        
# root = trie.root 
# print(root.children)
        
print(trie)
# print(reverse_trie)
