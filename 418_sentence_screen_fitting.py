#  [LeetCode] 418. Sentence Screen Fitting 

#  Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
# Note:

#     A word cannot be split into two lines.
#     The order of words in the sentence must remain unchanged.
#     Two consecutive words in a line must be separated by a single space.
#     Total words in the sentence won't exceed 100.
#     Length of each word is greater than 0 and won't exceed 10.
#     1 ≤ rows, cols ≤ 20,000.

# Example 1:

# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]

# Output: 
# 1

# Explanation:
# hello---
# world---

# The character '-' signifies an empty space on the screen.

# Example 2:

# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

# Output: 
# 2

# Explanation:
# a-bcd- 
# e-a---
# bcd-e-

# The character '-' signifies an empty space on the screen.

# Example 3:

# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

# Output: 
# 1

# Explanation:
# I-had
# apple
# pie-I
# had--

# The character '-' signifies an empty space on the screen.

class Solution(object):
    # https://www.cnblogs.com/grandyang/p/5975426.html
    # 思路是用start变量来记录下能装下的句子的总长度，最后除以一个句子的长度，就可以得到个数。
    # 而句子的总长度的求法时要在每个单词后面加上一个空格(包括最后一个单词)，
    # 我们遍历屏幕的每一行，然后每次start都加上宽度，然后看all[start%len]是否为空格，是的话就start加1，
    # 这样做的好处是可以处理末尾是没有空格的情况，
    # 比如宽度为1，只有一个单词a，那么我们都知道是这样放的 a ，
    # start变为1，len是2，all[start%len]是空格，所以start自增1，变成2，
    # 这样我们用start/len就知道能放下几个了。
    # 对于all[start%len]不为空格的情况，如果all[(start-1)%len]也不为空格，
    # 那么start就自减1，进行while循环，直至其为空格为止。
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int

        https://www.youtube.com/watch?v=kSlZlmuMdgE
        https://github.com/jzysheep/LeetCode/blob/master/418.%20Sentence%20Screen%20Fitting.cpp

        count: how many characters of the reformatted sentence is on the screen
        count % length of reformatted sentence: the starting position of the next row
        Answer: count / length of reformatted sentence

        ab cde f ab cde f ab cde f....
        XXX
           XXXX
               XXXXX
                    XXXX
                        XXXXX

        row 5
        col 4                        

        length: 9
        count = (3 + 4 + 5 + 4 + 5) / 9 = 2

        Count the total number of spaces used in the screen. 
        The spaces used in the screen are the ones occupied by characters 
        or the space between two words. 
        In other words, if the screen is m * n, then the total number of spaces is m * n. 
        But not all of those spaces are used. We need to discard the wasted spaces.
        After we got the number of spaces used, divide that by the length of the sentence.
        """
        # s = ''
        # for word in sentence:
        #     s += word
        #     s += ' '
        s = ' '.join(sentence) + ' '
        count = 0
        size = len(s)
        for _ in range(rows):
            count += cols
            if s[count % size] == ' ':
                count += 1
            else:
                while count > 0 and s[(count-1)%size] != ' ':
                    count -= 1

        return count // size

print (Solution().wordsTyping(["ab", "cde", "g"], 5, 4))
print (Solution().wordsTyping(["hello", "world"], 2, 8))
