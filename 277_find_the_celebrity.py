# 277. Find the Celebrity

# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one.
# The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B.
# You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) which tells you whether A knows B.
# Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

# Note: There will be exactly one celebrity if he/she is in the party.
# Return the celebrity's label if there is a celebrity in the party.
# If there is no celebrity, return -1.
#

# https://zhuhan0.blogspot.com/2017/07/leetcode-277-find-celebrity.html
# Thought process:

# Two pass. First pass find out the celebrity candidate. Second pass verify if candidate is truly a celebrity.
#
#     First pass: set candidate = 0. For each person on the right, check if they know the candidate.
#         If the person knows the candidate: continue.
#         Otherwise, we know the candidate cannot be the celebrity.
# We also know the people before the current person cannot be the celebrity because they know the candidate.
# So update the candidate to be the current person.
#         After the first pass, we know that only the candidate can be the celebrity,
# because the people before him/her cannot, and the people after can't be either because they know the candidate.

#     Second pass: check if the candidate knows any of the other people.
#
# Time complexity: O(n)

import random
def knows(a, b):
    return bool(random.getrandbits(1))
    # return random.choice([True, False])

class Solution:
    def findCelebrity(self, n):
        candidate = 0
        for i in range(1, n):
            if not knows(i, candidate):
                candidate = i

        for i in range(n):
            if (i != candidate and knows(candidate, i)) or not knows(i, candidate):
                return -1
        return candidate

s = Solution()
print(s.findCelebrity(1))
