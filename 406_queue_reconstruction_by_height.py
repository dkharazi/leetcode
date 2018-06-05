# 406. Queue Reconstruction by Height

# Suppose you have a random list of people standing in a queue. 
# Each person is described by a pair of integers (h, k), 
# where h is the height of the person 
# and k is the number of people in front of this person who have a height greater than or equal to h.
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


class Solution(object):
    # https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89345/Easy-concept-with-PythonC++Java-Solution

    #     1. Pick out tallest group of people and sort them in a subarray (S). 
    # Since there's no other groups of people taller than them, 
    # therefore each guy's index will be just as same as his k value.
    #     2. For 2nd tallest group (and the rest), 
    # insert each one of them into (S) by k value. So on and so forth.

    # E.g.
    # input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    # subarray after step 1: [[7,0], [7,1]]
    # subarray after step 2: [[7,0], [6,1], [7,1]]
    # subarray after step 3: [[5,0], [7,0], [5,2], [6,1], [7,1]]
    # ...

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        if not people:
            return res

        # height = []

        # key = height, value = [(k-value, index in original array)]
        peopledict = {}
        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledict:
                # peopledict[p[0]] += (p[1], i),
                peopledict[p[0]].append((p[1], i))
                
            else:
                peopledict[p[0]] = [(p[1], i)]
                # height += p[0],
                # height.append(p[0])
        # print(peopledict)

        heights = sorted(peopledict.keys(), reverse=True)
        for h in heights:
            peopledict[h].sort()    # sort the tuples
            for p in peopledict[h]:
                res.insert(p[0], people[p[1]])

        return res


print (Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
# [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
