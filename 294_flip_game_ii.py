# 294. Flip Game II

# You are playing the following Flip Game with your friend:
# Given a string that contains only these two characters: + and -,
# you and your friend take turns to flip twoconsecutive "++" into "--".
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# For example, given s = "++++", return true.
# The starting player can guarantee a win by flipping the middle "++" to become "+--+".
#
# Follow up:
# Derive your algorithm's runtime complexity.

class Solution:
    # https://gengwg.blogspot.com/2018/06/leetcode-294-flip-game-ii.html
    def canWin(self, s):
        n = len(s)
        s = list(s) # py string is not mutable
        for i in range(n-1):
            if s[i] == s[i+1] == '+':
                s[i] = '-'
                s[i+1] = '-'
                opponentWin = self.canWin(s)
                # restore original string
                s[i] = '+'
                s[i+1] = '+'
                if not opponentWin:
                    return True
        return False

    # https://github.com/criszhou/LeetCode-Python/blob/master/294.%20Flip%20Game%20II.py
    canWinCache = dict()
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<2:
            return False

        if s not in self.canWinCache:
            for i in range(len(s)-1):
                if s[i:i+2] == '++' and not self.canWin( s[:i]+'--'+s[i+2:] ):
                    ret = True
                    break
            else:
                ret = False
            self.canWinCache[s] = ret

        return self.canWinCache[s]

    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in self.canWinCache:
            return self.canWinCache[s]

        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                opponentWin = self.canWin( s[:i]+'--'+s[i+2:] )
                if not opponentWin:
                    self.canWinCache[s] = True
                    return True
        self.canWinCache[s] = False
        return False


print(Solution().canWin('++++'))
print(Solution().canWin('+++++'))
