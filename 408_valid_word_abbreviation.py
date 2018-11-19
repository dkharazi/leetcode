# 408 Valid Word Abbreviation

# Given a non-empty string s and an abbreviation abbr,
# return whether the string matches with the given abbreviation.
#
# A string such as “word” contains only the following valid abbreviations:
#
# [“word”, “1ord”, “w1rd”, “wo1d”, “wor1”, “2rd”, “w2d”, “wo2”, “1o1d”, “1or1”, “w1r1”, “1o2”, “2r1”, “3d”, “w3”, “4”]

# Notice that only the above abbreviations are valid abbreviations of the string “word”.
# Any other string is not a valid abbreviation of “word”.
#
# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.
#
#
# 虽然是一个easy 的题但却有两个坑：
# 1. abbr 结尾的地方是数字 例如：
#   s= "internationalization"   abbr=  "i5a11o1" , 因此 return时得加上cout 来判断  index + Integer.valueOf(count)
#   2.字符中 有 0， 例如 s= "a"  abbr= "01" 因此只要出现一个不是其他数字后面的0 都是非法的， 比如 01 非法， 而10 合法。加上这个判断

class Solution:
    def validWordAbbreviation(self, word, abbr):
        index = 0   # current position in `word`
        count = '0' # numbers in `abbr`

        for c in abbr:
            if not str.isdigit(c):
                index += int(count)
                if index >= len(word) or c != word[index]:
                    return False
                # reset count to 0 and increment index by 1
                count = '0'
                index += 1
            else:
                if count == '0' and c == '0':
                    return False
                count += c
        # remember to add the final count (if not 0)
        return index + int(count) == len(word)


sol = Solution()
print(sol.validWordAbbreviation(word="internationalization", abbr="i5a11o1"))
print(sol.validWordAbbreviation(word="word", abbr="w2d"))
print(sol.validWordAbbreviation(word="a", abbr="1"))
print(sol.validWordAbbreviation(word="a", abbr="01"))
