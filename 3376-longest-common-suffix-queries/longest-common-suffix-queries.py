class TrieNode(object):

    def __init__(self):
        self.index = -1
        self.length = float('inf')
        self.children = [None] * 26


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    # Insert word from right to left
    def insert(self, string, ind):

        node = self.root
        str_len = len(string)

        for i in range(str_len - 1, -1, -1):

            ch = ord(string[i]) - ord('a')

            if node.children[ch] is None:
                node.children[ch] = TrieNode()

            node = node.children[ch]

            # Store shortest string info
            if str_len < node.length:
                node.length = str_len
                node.index = ind

    # Search longest matching suffix
    def prefix(self, query):

        node = self.root
        result = -1

        for i in range(len(query) - 1, -1, -1):

            ch = ord(query[i]) - ord('a')

            if node.children[ch] is None:
                break

            node = node.children[ch]
            result = node.index

        return result


class Solution(object):

    def stringIndices(self, words, query):

        trie = Trie()

        index = -1
        smallest = float('inf')

        # Insert all words into trie
        for i in range(len(words)):

            trie.insert(words[i], i)

            # Track globally smallest word
            if len(words[i]) < smallest:
                smallest = len(words[i])
                index = i

        ans = [0] * len(query)

        # Process each query
        for i in range(len(query)):

            ind = trie.prefix(query[i])

            # If no suffix found
            if ind == -1:
                ans[i] = index
            else:
                ans[i] = ind

        return ans