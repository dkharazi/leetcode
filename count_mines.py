'''
Count the Mines Problem:

Your program will first read an integer N from stdin.
Then it will then read N lines of N integers separated by spaces.
Each integer in this Grid will be either 1 or 0.

The program then outputs an N x N Grid where each Grid element represents the number of 1's surrounding that element, (excluding the element itself).

For (column, row) = (0, 0), surrounding element indices are (0,1) (1,0) and (1,1).
Similarly for (1,1), surrounding element indices are  (0,0) (0,1) (0,2) (1,0) (1,2) (2,0) (2,1) and (2,2).

Constraints:

Your output lines should not have any trailing or leading white space
Maximum Dimension of Grid = 1000 x 1000

Example Input:

3
0 1 0
0 0 0
1 0 0
Example Output:

1 0 1
2 2 1
0 1 0
'''
#!/usr/bin/env python
import sys

mine_input = []

# Input
rows = int(sys.stdin.readline())
for _ in range(rows):
    row = sys.stdin.readline()
    mine_input.extend(row.strip().split(' '))
# make all inputs integer values
mine_input = [ int(x) for x in mine_input]

# There are two cases for 'surrounding':
# 1. in same row:
#       i +- 1 (2 max)
# 2. in ajacent rows:
#       i +- row +- [0,1] (6 max)
mine_output = []
for i in range(len(mine_input)):
    # same row
    surround1 = list(set([i+1, i-1]))
    # rows diff by 1
    surround2 = list(set([i+rows, i-rows, i+rows+1, i+rows-1, i-rows+1, i-rows-1]))

    # filter each case
    surround1_filter = filter(lambda x: x != i and x >= 0 and x <= len(mine_input)-1 and i/rows == x/rows, surround1)
    surround2_filter = filter(lambda x: x != i and x >= 0 and x <= len(mine_input)-1 and abs(i/rows - x/rows) == 1, surround2)

    surround_indexes = surround1_filter + surround2_filter
    #print surround_indexes
    sum = 0
    for j in surround_indexes:
        sum += mine_input[j]
    mine_output.append(sum)

#print mine_output

# Output
count = 0
for char in mine_output:
    count += 1
    if count % rows == 0:
        print char
    else:
        print char,

"""
Sample:
3
1 1 1
1 1 1
1 1 1
3 5 3
5 8 5
3 5 3

5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
3 5 5 5 3
5 8 8 8 5
5 8 8 8 5
5 8 8 8 5
3 5 5 5 3
"""
