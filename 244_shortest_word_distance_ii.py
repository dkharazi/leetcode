"""
244 Shortest Word Distance II

This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words
and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor,
and implements a method that takes two words word1 and word2
and return the shortest distance between these two words in the list.

For example,
Assume that words = [“practice”, “makes”, “perfect”, “coding”, “makes”].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = “makes”, word2 = “coding”, return 1.

Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.


If the function is going to be called multiple times, then we need to store information that can be calculated already.
In this case, we use a HashMap to keep track of all the appearing index for a certain element.
"""

from collections import defaultdict

class wordDistance:
    def __init__(self, words):
        self.indexes = {}
        for i, word  in enumerate(words):
            if word not in self.indexes:
                self.indexes[word] = [i]
            else:
                self.indexes[word].append(i)

        self.indexes = defaultdict(list)
        for i, w in enumerate(words):
            self.indexes[w].append(i)

    def shortest(self, word1, word2):
        indexes1 = self.indexes.get(word1)
        indexes2 = self.indexes.get(word2)
        ans = 100
        for i1 in indexes1:
            for i2 in indexes2:
                ans = min(ans, abs(i1 - i2))
        return ans

    # replace above for loop with indexing to reduce complexity from O(N^2) to O(1)
    # taking advantage of both indexes are sorted, and both words are in the list
    def shortest(self, word1, word2):
        indexes1 = self.indexes.get(word1)
        indexes2 = self.indexes.get(word2)
        ans = min(abs(indexes1[0] - indexes2[-1]), abs(indexes2[0] - indexes1[-1]))
        return ans

# Your WordDistance object will be instantiated and called as such:
# WordDistance wordDistance = new WordDistance(words);
# wordDistance.shortest("word1", "word2");
# wordDistance.shortest("anotherWord1", "anotherWord2");
wd = wordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(wd.shortest("coding", "practice"))
print(wd.shortest("coding", "makes"))


