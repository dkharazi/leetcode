#  251. Flatten 2D Vector

# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]

# By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,2,3,4,5,6].

# Hint:

#     How many variables do you need to keep track?
#     Two variables is all you need. Try with x and y.
#     Beware of empty rows. It could be the first few rows.
#     To write correct code, think about the invariant to maintain. What is it?
#     The invariant is x and y must always point to a valid point in the 2d vector.
# Should you maintain your invariant ahead of time or right when you need it?
#     Not sure? Think about how you would implement hasNext(). Which is more complex?
#     Common logic in two different places should be refactored into a common method.

# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.

class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.row = 0
        self.col = 0
        self._moveToValid()

    def _moveToValid(self):
        """
        move i and j to a valid position, so that self.vec2d[self.i][self.j] is valid.
        this also takes care of case such as [[], [2, 3]] at initialization.
        """
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec2d[self.row][self.col]
        self.col += 1
        self._moveToValid()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.row < len(self.vec2d)


# use list comprehension. operations not in place
class Vector2D(object):
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.vec1d = [x for y in self.vec2d for x in y]

    def next(self):
        return self.vec1d.pop(0)

    def hasNext(self):
        return len(self.vec1d) > 0

# Your Vector2D object will be instantiated and called as such:
if __name__ == '__main__':
    vec2d = [
        [1,2],
        [3],
        [],
        [4,5,6],
        []
    ]
    # vec2d = [[3]]
    # vec2d = [[],[1,2,3],[4,5],[],[],[6],[7,8],[],[9],[10],[]]
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print(v)
