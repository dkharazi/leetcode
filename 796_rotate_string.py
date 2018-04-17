# 796. Rotate String

# We are given two strings, A and B.

# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
# Return True if and only if A can become B after some number of shifts on A.

# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true

# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# Note:
# A and B will have length at most 100.

# --------------------------
# Given two string s1 and s2 how will you check if s1 is a rotated version of s2 ?
# 
# Example:
# 
# If s1 = "stackoverflow" then the following are some of its rotated versions:
# 
# "tackoverflows"
# "ackoverflowst"
# "overflowstack"
# where as "stackoverflwo" is not a rotated version.

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        return len(A) == len(B) and A in B * 2  

def isRotation(s1, s2):
    for i in range(0, len(s1)):
        s3 = s1[-i:] + s1[:-i]
        if s3 == s2:
            return True
    return False

def isRotation(s1, s2):
    return len(s1) == len(s2) and s1 in s2 * 2

def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s1 in s2 * 2

if __name__ == '__main__':
    s1 = "stackoverflow"
    print isRotation(s1, "tackoverflows")
    print isRotation(s1, "ackoverflowst")    
    print isRotation(s1, "overflowstack")
    print isRotation(s1, "stackoverflwo")
    
