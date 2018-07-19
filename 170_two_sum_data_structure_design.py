# Design and implement a TwoSum class.
# It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
#

import collections

class TwoSum:
    def __init__(self):
        # initialize dict with default value 0 for any key
        self.table = collections.defaultdict(int)

    def add(self, number):
        self.table[number] += 1

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for key in self.table:
            num = value - key
            # num diff than key, or
            # num == key, and more than one keys
            if num in self.table and (num != key or self.table[key] > 1):
                return True
        return False

if __name__ == "__main__":
    Sol = TwoSum()

    Sol.add(1)
    for i in (1, 3, 5):
        Sol.add(i)

    for i in (4, 7):
        print("{}: {}".format(i, Sol.find(i)))
