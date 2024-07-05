# Time Complexity : O(nxl) for Insert function, where n is the number of words in the dictionary and l is the average length of the words. O(mxl) for Replace Words function, where m is the number of words in the sentence and l is the average length of the words
# Space Complexity : O(nxl) for Insert and O(mxl) for Replace Words

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26  # 26 because only lowercase letters used

class Solution:
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

    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        # Base case
        if not dictionary or not sentence:
            return sentence
        
        # Build the Trie from the dictionary
        for word in dictionary:
            self.insert(word)
        
        # Split the sentence into words
        strArr = sentence.split(" ")
        result = []
        
        # Replace words in the sentence with the shortest root in the Trie
        for word in strArr:
            cur = self.root
            replacement = []
            for ch in word:
                index = ord(ch) - ord('a')
                if cur.children[index] is None or cur.isEnd:
                    break
                replacement.append(ch)
                cur = cur.children[index]
            if cur.isEnd:
                result.append("".join(replacement))
            else:
                result.append(word)
        
        return " ".join(result)

# Example usage

# Example 1
solution = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(solution.replaceWords(dictionary, sentence))  # Expected Output: "the cat was rat by the bat"

# Example 2
solution = Solution()
dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(solution.replaceWords(dictionary, sentence))  # Expected Output: "a a b c"

# Example 3
solution = Solution()
dictionary = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
print(solution.replaceWords(dictionary, sentence))  # Expected Output: "a a a a a a a a bbb baba a"