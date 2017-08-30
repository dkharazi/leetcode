# -*- coding: utf-8 -*-
# 134. Gas Station
#
# There are N gas stations along a circular route,
# where the amount of gas at station i is gas[i].
#
# You have a car with an unlimited gas tank
# and it costs cost[i] of gas to travel from station i to its next station (i+1).
# You begin the journey with an empty tank at one of the gas stations.
#
# Return the starting gas station's index
# if you can travel around the circuit once,
# otherwise return -1.
#
# Note:
# The solution is guaranteed to be unique.


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(gas) < sum(cost):
            return -1
        min_sum, min_index, total = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if min_sum > total:
                min_sum, min_index = total, i + 1

        return -1 if total < 0 else min_index


if __name__ == "__main__":
    assert Solution().canCompleteCircuit([5], [4]) == 0
    assert Solution().canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
"""
https://shenjie1993.gitbooks.io/leetcode-python/134%20Gas%20Station.html
选择从一个加油站出发，如果车要能够到达下一个加油站，就需要这个加油站的gas>cost。
不妨设c[i] = gas[i] - cost[i]，c[i]表示的是从某一加油站得到的汽油减去到达下一个加油站需要耗费的汽油后剩余的汽油数目，
对c求和得到的是从出发开始到当前加油站剩余的汽油数目，
如果这个这个和为负，说明当前这种行驶方案无法到达当前的加油站。
也就是说要使车能够不断的向前行进，就要保证途中对c的求和始终大于0。
如果cost的和大于gas的和，显然汽车是无法成功走完一圈的，
下面证明如果cost的和小于等于gas的和，必然存在一种方案能够让汽车走完一圈。

现在有c[0]+c[1]+...+c[n-2]+c[n-1]>=0，
我们对c的前i项求和，假设当i=j时，这个和是所有和中最小的，也就是说：
c[0]+c[1]+...+c[j-1]<=c[0]+c[1]+...c[j]
c[0]+c[1]+...+c[j-1]<=c[0]+c[1]+...c[j]+c[j+1]
...
c[0]+c[1]+...+c[j-1]<=c[0]+c[1]+...c[j]+c[j+1]+...+c[n-1]

也就是说：
c[j]>=0
c[j]+c[j+1]>=0
...
c[j]+c[j+1]+...+c[n-1]>=0

同时，因为前j项的求和是最小的，还能得到下面的不等式：
c[0]+c[1]+...+c[j-1]<=c[0]+c[1]+...+c[j-2]
c[0]+c[1]+...+c[j-1]<=c[0]+c[1]+...+c[j-3]
...
c[0]+c[1]+...+c[j-1]<=c[0]

转换可以得到：
c[j-1]<=0
c[j-2]+c[j-1]<=0
...
c[1]+c[1]+...+c[j-1]<=0

再组合最初始的条件c[0]+c[1]+...+c[n-2]+c[n-1]>=0，我们可以得到：
c[j]+c[j+1]+...+c[n-1]+c[0]+c[1]+...+c[j-2]>=0
c[j]+c[j+1]+...+c[n-1]+c[0]+c[1]+...+c[j-3]>=0
c[j]+c[j+1]+...+c[n-1]+c[0]>=0
至此我们可以看出，如果从j出发的话，对c的求和始终都满足大于等于零的要求，
也就是说j是我们选择出发的加油站。"""
