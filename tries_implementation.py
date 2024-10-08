class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word


    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word


trie = TrieTree()
trie.insert("apple")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))    # Output: False
print(trie.startsWith("app"))  # Output: True
trie.insert("app")
print(trie.search("app"))    # Output: True
