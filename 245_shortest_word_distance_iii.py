"""
243 Shortest Word Distance III

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note:
You may assume word1 and word2 are both in the list.
"""
class Solution:
    # @param {string[]} words
    # @param {string} word1
    # @param {string} word2
    # @return {integer}

    # 用p1, p2两个pointer记录word1，word2最后一次出现的位置。
    # 最短路径就是所有|p1 - p2|中的最小值
    # 如果word1跟word2相同，p1指向p2的上一个位置，p2更新为新位置就可以了
    def shortestDistance(self, words, word1, word2):
        a = b = -1
        ans = len(words)

        for i in range(len(words)):
            if words[i] == word1:
                a = i
            if words [i] == word2:
                if word1 == word2:
                    a = b
                b = i

            if a >= 0 and b >= 0:
                ans = min(ans, abs(a - b))
        return ans

if __name__ == "__main__":
    solution = Solution()

    words =  ["practice", "makes", "perfect", "coding", "makes"]
    print('The given a list of words: {}'.format(words))

    word1 = "coding"
    word2 = "practice"
    print('Distance between "{}" and "{}":'.format(word1, word2))
    print(solution.shortestDistance(words, word1, word2))

    word1 = "coding"
    word2 = "makes"
    print('Distance between "{}" and "{}":'.format(word1, word2))
    print(solution.shortestDistance(words, word1, word2))

    word1 = "makes"
    word2 = "makes"
    print('Distance between "{}" and "{}":'.format(word1, word2))
    print(solution.shortestDistance(words, word1, word2))


