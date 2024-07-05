# Time Complexity : O(nxl), where n is the number of words and l is the average length of the words
# Space Complexity : O(nxl), for the Trie

from collections import deque

class Solution:
    class TrieNode:
        def __init__(self):
            self.is_end = False
            self.children = [None] * 26

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if cur.children[index] is None:
                cur.children[index] = self.TrieNode()
            cur = cur.children[index]
        cur.is_end = True

    def longestWord(self, words):
        if not words:
            return ""
        
        self.root = self.TrieNode()
        longest = ""
        queue = deque([(self.root, "")])

        for word in words:
            self.insert(word)
        
        while queue:
            cur, cur_word = queue.popleft()
            for i in range(25, -1, -1):
                if cur.children[i] and cur.children[i].is_end:
                    next_word = cur_word + chr(i + ord('a'))
                    queue.append((cur.children[i], next_word))
                    if len(next_word) > len(longest) or (len(next_word) == len(longest) and next_word < longest):
                        longest = next_word

        return longest

# Example 1
words1 = ["w","wo","wor","worl","world"]
sol1 = Solution()
print(sol1.longestWord(words1))  # Output: "world"

# Example 2
words2 = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
sol2 = Solution()
print(sol2.longestWord(words2))  # Output: "apple"

# Example 3
words3 = ["t", "ti", "tig", "tige", "tiger"]
sol3 = Solution()
print(sol3.longestWord(words3))  # Output: "tiger"