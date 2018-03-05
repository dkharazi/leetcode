# -*- coding: utf-8 -*-
"""
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

http://www.cnblogs.com/zuoyuan/p/3777289.html

解题思路：
题目的要求是输出Unix下的最简路径，
Unix文件的根目录为"/"，"."表示当前目录，".."表示上级目录。

例如：

输入1：
/../a/b/c/./..

输出1：
/a/b

模拟整个过程：

1. "/" 根目录

2. ".." 跳转上级目录，上级目录为空，所以依旧处于 "/"

3. "a" 进入子目录a，目前处于 "/a"

4. "b" 进入子目录b，目前处于 "/a/b"

5. "c" 进入子目录c，目前处于 "/a/b/c"

6. "." 当前目录，不操作，仍处于 "/a/b/c"

7. ".." 返回上级目录，最终为 "/a/b"

使用一个栈来解决问题。
遇到'..'弹栈，
遇到'.'不操作，
其他情况下压栈。
"""


class Solution(object):
    # python has built-in function for this
    def simplifyPath(self, path):
        import os.path
        return os.path.normpath(path)

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        i = 0
        res = ''

        while i < len(path):
            # calculate end of sub path at position i
            end = i + 1
            while end < len(path) and path[end] != "/":
                end += 1
            sub = path[i + 1:end]

            if len(sub) > 0:
                # if .., pop stack
                if sub == "..":
                    if stack != []:
                        stack.pop()
                # if not ., push(append) stack
                elif sub != ".":
                    stack.append(sub)

            # advance to end of sub path
            i = end

        if stack == []:
            return "/"
        # construct abs path
        for i in stack:
            res += "/" + i
        return res

    # https://gengwg.blogspot.com/2018/03/leetcode-71-simplify-path.html
    def simplifyPath(self, path):
        stack = []
        res = ''
        # split path by / and filter out empty and .
        # so that only alphanumerical and .. left
        items = filter(lambda x: x not in ['', '.'], path.split('/'))
        for item in items:
            if item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        if not stack:
            return "/"
        # construct abs path
        for item in stack:
            res += "/" + item
        return res


if __name__ == '__main__':
    print Solution().simplifyPath("/../a//b/c/./..")
    print Solution().simplifyPath("/../")
    print Solution().simplifyPath(".")
