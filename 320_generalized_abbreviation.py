# 320. Generalized Abbreviation

# Write a function to generate the generalized abbreviations of a word.

# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def dfs(word, i, cur, res):
            if i == len(word):
                res.append(''.join(cur))
                return
            cur.append(word[i])
            dfs(word, i+1, cur, res)
            cur.pop()
            if not cur or not cur[-1][-1].isdigit():
                for l in range(1, len(word)-i+1):
                    cur.append(str(l))
                    dfs(word, i+l, cur, res)
                    cur.pop()

        res, cur = [], []
        dfs(word, 0, cur, res)
        return res

    # https://github.com/jzysheep/LeetCode/blob/master/320.%20Generalized%20Abbreviation.cpp
    # https://gengwg.blogspot.com/2018/06/leetcode-320-generalized-abbreviation.html
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]

        time O(2^n)

        pos: points to the current character
        cur: current string formed
        count: how many letters are abbreviated in the current streak

        At each step:
            Abbreviate the current letter
            Keep the current letter and summarize the abbreviation in the current streak
        """
        def dfs(res, word, i, cur, count):
            if i == len(word):
                if count > 0:
                    cur += str(count)
                res.append(cur)
                return

            # abbreviate this letter
            dfs(res, word, i+1, cur, count+1)

            # keeep this letter, summarize the abbreviation in the current streak
            if count > 0:
                cur += str(count)
            cur += word[i]

            dfs(res, word, i+1, cur, 0)

        res = []
        dfs(res, word, 0, '', 0)
        return res

print Solution().generateAbbreviations('word')
