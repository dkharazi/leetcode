# 336. Palindrome Pairs

# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
#
# Example 2:
#
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
#
class Solution(object):
    # http://bookshadow.com/weblog/2016/03/10/leetcode-palindrome-pairs/
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 利用字典wmap保存单词 -> 下标的键值对
        wmap = {y:x for x,y in enumerate(words)}

        def isPalindrome(word):
            size = len(word)
            for x in range(size//2):
                if word[x] != word[size - x - 1]:
                    return False
            return True

        ans = set()

        # 遍历单词列表words，记当前单词为word，下标为idx
        for idx, word in enumerate(words):
            # 若当前单词word本身为回文，且words中存在空串，则将空串下标bidx与idx加入答案
            if "" in wmap and word != "" and isPalindrome(word):
                bidx = wmap[""]
                ans.add((bidx, idx))
                ans.add((idx, bidx))

            # 若当前单词的逆序串在words中，则将逆序串下标ridx与idx加入答案
            rword = word[::-1]
            if rword in wmap:
                ridx = wmap[rword]
                if idx != ridx:
                    ans.add((idx, ridx))
                    ans.add((ridx, idx))

            for i in range(1, len(word)):
                # 将当前单词word拆分为左右两半left，right
                left, right = word[:i], word[i:]
                # reverse string of left and right substrings
                rleft, rright = left[::-1], right[::-1]
                # 若left为回文，并且right的逆序串在words中
                if isPalindrome(left) and rright in wmap:
                    # 则将right的逆序串下标rridx与idx加入答案
                    ans.add((wmap[rright], idx))
                # 若right为回文，并且left的逆序串在words中，
                if isPalindrome(right) and rleft in wmap:
                    # 则将left的逆序串下标idx与rlidx加入答案
                    ans.add((idx, wmap[rleft]))

        return list(ans)


sol = Solution()
print(sol.palindromePairs(["abcd","dcba","lls","s","sssll"]))
print(sol.palindromePairs(["abcd","dcba","ll","s", ""]))
print(sol.palindromePairs(["bat","tab","cat"]))
