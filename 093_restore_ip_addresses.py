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
        def dfs(s, count, ips, ip):
            if count == 4:
                if s == '':
                    ips.append(ip[1:])  # remove first .
                else:   # do nothing
                    return
            for i in range(1, 4):   # each section is possibly 1, 2, 3 digits
                # each section must be smaller than 255. i must be inside also
                if i <= len(s) and int(s[:i]) <= 255:
                    # call self before next line to get '0.0.0.0', not '00.0.0.0'
                    dfs(s[i:], count + 1, ips, ip + '.' + s[:i])
                    if s[0] == '0':
                        break

        ips = []
        dfs(s, 0, ips, '')
        return ips


if __name__ == '__main__':
    print Solution().restoreIpAddresses("25525511135")
