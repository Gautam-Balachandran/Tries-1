# Time Complexity : O(l), for all 3 operations, where l is the length of the word
# Space Complexity : O(nxl), where n is the number of words inserted into the Trie, and l is the average length of the inserted word

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26  # Because only lowercase letters are used

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        return True

# Example usage
trie = Trie()

# Example 1: Insert and search
trie.insert("apple")
print(trie.search("apple"))    # Expected Output: True
print(trie.search("app"))      # Expected Output: False
print(trie.startsWith("app"))  # Expected Output: True

# Example 2: Insert another word and search
trie.insert("app")
print(trie.search("app"))      # Expected Output: True

# Example 3: Insert a different word and search
trie.insert("banana")
print(trie.search("banana"))   # Expected Output: True
print(trie.search("ban"))      # Expected Output: False
print(trie.startsWith("ban"))  # Expected Output: True