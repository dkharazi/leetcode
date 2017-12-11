"""
243 Shortest Word Distance

Question:
    Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

    For example,
    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Given word1 = "coding", word2 = "practice", return 3.
    Given word1 = "makes", word2 = "coding", return 1.

    Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

    Hints:
    Two variable to track the last positions.

    Complexity:
    O(n) time
    O(1) space
"""

class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def shortestDistance(self, words, word1, word2):
        a = b = -1
        ans = len(words)
        #ans = 0 # when used for searching largest distance

        for i in range(len(words)):
            if words[i] == word1:
                a = i
            elif words [i] == word2:
                b = i

            #print i, a, b
            if a >= 0 and b >= 0:
                ans = min(ans, abs(a - b))
                # ans = max(ans, abs(a - b))
        return ans

if __name__ == "__main__":
    solution = Solution()

    words =  ["practice", "makes", "perfect", "coding", "makes"]
    print 'The given a list of words: {}'.format(words)

    word1 = "coding"
    word2 = "practice"
    print 'Distance between "{}" and "{}":'.format(word1, word2)
    print solution.shortestDistance(words, word1, word2)

    word1 = "coding"
    word2 = "makes"
    print 'Distance between "{}" and "{}":'.format(word1, word2)
    print solution.shortestDistance(words, word1, word2)

