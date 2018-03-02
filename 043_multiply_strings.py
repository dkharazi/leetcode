# -*- coding: utf-8 -*-

"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

http://www.cnblogs.com/zuoyuan/p/3781515.html
解题思路：两个非负数字字符串的相乘。
其实就是大数乘法。
算法的关键是要先将两个字符串翻转过来，然后按位进行相乘，
相乘后的数不要着急进位，而是存储在一个数组里面，
然后将数组中的数对10进行求余（%），就是这一位的数，
然后除以10，即/10，就是进位的数。
注意最后要将相乘后的字符串前面的0去掉。

http://blog.csdn.net/chhuach2005/article/details/21168179

乘积是逐位相乘，也就是aibj，结果加入到积C的第i+j位，最后处理进位即可
例如：
A =17 = 1*10 + 7 = （7,1）
(最后是十进制的幂表示法，幂次是从低位到高位，以下同。)
B = 25 = 2*10 + 5 = (5, 2);
C = A * B
= (7 * 5, 1 * 5 + 2 * 7, 1 * 2)
= (35, 19, 2)
= (5, 22, 2)
= (5, 2. 4)
= 425。

原博客的思路为：
（1）转换并反转，字符串转换为数字并将字序反转；

（2）逐位相乘，结果存放在result_num[i+j]中；

（3）处理进位，消除多余的0；

（4）转换并反转，将计算结果转换为字符串并反转。


"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = num1[::-1]; num2 = num2[::-1]

        arr = [0 for _ in range(len(num1) + len(num2))]
        # multiply by digit and store result at arr[i+j]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])

        ans = []
        # process carrying
        for i in range(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] / 10
            if i < len(arr) - 1: # ?
                arr[i + 1] += carry
            # insert to the front, effectively reverse arr.
            ans.insert(0, str(digit))

        # remove leading 0s
        while ans[0] == '0' and len(ans) > 1:
            del ans[0]

        return ''.join(ans)

if __name__ == '__main__':
    print Solution().multiply('100', '200')