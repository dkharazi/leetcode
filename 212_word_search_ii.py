# 212. Word Search II
#
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
# click to show hint.
#
# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
#
# If the current candidate does not exist in all words' prefix, you could stop backtracking immediately.
# What kind of data structure could answer such query efficiently?
# Does a hash table work? Why or why not? How about a Trie?
# If you would like to learn how to implement a basic trie, please work on this problem:
# Implement Trie (Prefix Tree) first.
#


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def delete(self, word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node))
            child = node.childs.get(letter)
            if child is None:
                return False
            node = child
        if not node.isWord:
            return False
        if len(node.childs):
            node.isWord = False
        else:
            for letter, node in reversed(queue):
                del node.childs[letter]
                if len(node.childs) or node.isWord:
                    break
        return True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        w, h = len(board[0]), len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)

        visited = [[False] * w for x in range(h)]
        dz = zip([1, 0, -1, 0], [0, 1, 0, -1])
        ans = []

        def dfs(word, node, x, y):
            node = node.childs.get(board[x][y])
            if node is None:
                return
            visited[x][y] = True
            for z in dz:
                nx, ny = x + z[0], y + z[1]
                if nx >= 0 and nx < h and ny >= 0 and ny < w and not visited[nx][ny]:
                    dfs(word + board[nx][ny], node, nx, ny)
            if node.isWord:
                ans.append(word)
                trie.delete(word)
            visited[x][y] = False

        for x in range(h):
            for y in range(w):
                dfs(board[x][y], trie.root, x, y)

        return sorted(ans)


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]

    print Solution().findWords(board, words)
