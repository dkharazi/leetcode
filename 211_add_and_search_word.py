# 211. Add and Search Word - Data structure design
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
#
# search(word) can search a literal word or a regular expression string containing
# only letters a-z or .. A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#
# click to show hint.
#
# You should be familiar with how a Trie works. If not, please work on this problem: Implement Trie (Prefix Tree) first.
#
# http://bookshadow.com/weblog/2015/05/16/leetcode-add-and-search-word-data-structure-design/


class TrieNode(object):
    def __init__(self):
        self.children = {}
        #self.children = dict()
        self.isWord = False


class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if node.children.get(letter) is None:
                node.children[letter] = TrieNode()  # add a new trie node
            node = node.children.get(letter)    # move node to next level
        node.isWord = True  # set the last node to true

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.find(self.root, word)

    # dfs
    def find(self, node, word):
        if word == '':  # termination condition
            return node.isWord
        if word[0] == '.':  # if . loop over all children
            for x in node.children:
                if x and self.find(node.children[x], word[1:]):
                    return True
        else:   # normal find
            child = node.children.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    print obj.search("pad")
    print obj.search(".ad")
