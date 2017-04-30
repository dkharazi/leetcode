"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

Author: gengwg[at]gmail.com
"""

from collections import Counter

l = [(1,3), (2,6), (8,10), (15,18)]

# flatten the list
flat = [x for _ in l for x in _]
# sort set flatted list (ssf)
ssf = sorted(set(flat))

to_remove = []

c = Counter(flat)
for x in c:
    # remove all elements appeared more than once,
    # but only in the middle,
    # which would be the border of two intervals
    if c[x] > 1 and x in ssf[1:-1]:
        to_remove.append(x)

# loop over all intervals
# if any x in ssf is within any interval
# it needs to be removed
for x in ssf:
    for y in l:
        if y[0] < x < y[1]:
            to_remove.append(x)

# remove above selected
for x in set(to_remove):
    ssf.remove(x)

# zip even numbers with odd numbers
# the final result are guarrantted to be even numbers
# due to the intervals are pairs..
print zip(ssf[0::2], ssf[1::2])
