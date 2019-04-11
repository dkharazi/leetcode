# 751. IP to CIDR
#
# Given a start IP address ip and a number of ips we need to cover n,
# return a representation of the range as a list (of smallest possible length) of CIDR blocks.
#
# A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length.
# For example: "123.45.67.89/20". That prefix length "20" represents the number of
# common prefix bits in the specified range.
#
# Example 1:
#
# Input: ip = "255.0.0.7", n = 10
# Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]

# Explanation:
# The initial ip address, when converted to binary, looks like this (spaces added for clarity):
# 255.0.0.7 -> 11111111 00000000 00000000 00000111
# The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
# ie. just this one address.
#
# The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
# 255.0.0.8 -> 11111111 00000000 00000000 00001000
# Addresses with common prefix of 29 bits are:
# 11111111 00000000 00000000 00001000
# 11111111 00000000 00000000 00001001
# 11111111 00000000 00000000 00001010
# 11111111 00000000 00000000 00001011
# 11111111 00000000 00000000 00001100
# 11111111 00000000 00000000 00001101
# 11111111 00000000 00000000 00001110
# 11111111 00000000 00000000 00001111
#
# The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
# ie. just 11111111 00000000 00000000 00010000.
#
# In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .
#
# There were other representations, such as:
# ["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
# but our answer was the shortest possible.
#
# Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
# because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100
# that are outside the specified range.
#
# Note:
#
#     ip will be a valid IPv4 address.
#     Every implied address ip + x (for x < n) will be a valid IPv4 address.
#     n will be an integer in the range [1, 1000].
#

class Solution(object):
    # 将起始ip转为int，遍历[ipInt, ipInt + range)
    #
    # 假设当前遍历到了第x个ip地址，记cIpInt = ipInt + x
    #
    # 计算cIpInt末尾0的个数，记为zeros，重复将zeros-1，直到x + 1<<zeros不大于range为止
    #
    # 将ipInt复原为IP地址 / 32 - zeros加入结果列表]
    def ipToCIDR(self, ip, range):
        """
        :type ip: str
        :type range: int
        :rtype: List[str]
        """
        ipInt = self.ip2int(ip)
        ans = []
        x = 0
        while x < range:
            zeros = self.countZeros(ipInt + x)
            while x + (1 << zeros) > range:
                zeros -= 1
            ans.append(self.int2ip(ipInt + x) + '/' + str(32 - zeros))
            x += 1 << zeros
        return ans

    def ip2int(self, ip):
        """
        convert ip to integer
        """
        ans = 0
        for idx, part in enumerate(ip.split('.')[::-1]):
            ans += int(part) << idx * 8
            # ans = ans + (int(part) << (idx * 8))
        return ans

    def int2ip(self, ipInt):
        """
        convert integer to ip
        """
        ans = []
        for x in range(4):
            ans.append((ipInt >> x * 8) & 255)
        return '.'.join(map(str, ans[::-1]))

    def countZeros(self, ip):
        """
        count trailing 0s in ip
        """
        cnt = 0
        while ip:
            if ip & 1: break
            cnt += 1
            ip >>= 1
        return cnt

sol = Solution()
print(sol.ip2int('255.0.0.7'))
print("{0}".format(sol.int2ip(4278190087)))
print(sol.ipToCIDR('255.0.0.7', 10))
print(sol.ipToCIDR('255.0.0.7', 30))

