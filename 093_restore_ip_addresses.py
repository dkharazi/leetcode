"""
93. Restore IP Addresses

Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"].
(Order does not matter)

http://www.cnblogs.com/zuoyuan/p/3768112.html
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s, sub, ips, ip):
            if sub == 4:
                if s == '':
                    ips.append(ip[1:])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub + 1, ips, ip + '.' + s[:i])
                    if s[0] == '0':
                        break

        ips = []
        dfs(s, 0, ips, '')
        return ips


if __name__ == '__main__':
    print Solution().restoreIpAddresses("25525511135")
