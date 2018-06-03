# 271. Encode and Decode String

# Design an algorithm to encode a list of strings to a string. 
# The encoded string is then sent over the network 
# and is decoded back to the original list of strings.

# Machine 1 (sender) has the function:

# string encode(vector strs) {
#   // ... your code
#   return encoded_string;
# }

# Machine 2 (receiver) has the function:

# vector decode(string s) {
#   //... your code
#   return strs;
# }

# So Machine 1 does:

# string encoded_string = encode(strs);

# and Machine 2 does:

# vector strs2 = decode(encoded_string);

# strs2 in Machine 2 should be the same as strs in Machine 1.

# Implement the encode and decode methods.

# Note:

#     The string may contain any possible characters out of 256 valid ascii characters. 
# Your algorithm should be generalized enough to work on any possible characters.
#     Do not use class member/global/static variables to store states. 
# Your encode and decode algorithms should be stateless.
#     Do not rely on any library method such as eval or serialize methods. 
# You should implement your own encode/decode algorithm.

# https://gengwg.blogspot.com/2018/06/leetcode-271-encode-and-decode-strings.html
# 用长度+特殊字符+字符串来编码
class Codec(object):
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        Algorithm: Length info
        :type strs: List[str]
        :rtype: str

        To encode the string, we can add some symbols before it. 
        For example, for string “abc”, we can add the length 3 before it. 
        However, for string starting from numbers, like 123abc. 
        This could result in 6123abc, which is not acceptable. 
        Then we add an ‘#’ between the length and the string.  
        So 3#abc is the encoded string.

        To decode the string, we can search the ‘#’ symbol. 
        The number before it is the length for the string, 
        and the string after it with length is the string we want to decode.
        """
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '/' + s
        return encoded

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        decoded = []
        j = 0
        for i, c in enumerate(s):
            if c == '/':
                offset = int(s[j:i])
                decoded.append(s[i+1:i+offset+1])
                j = i+offset+1
        return decoded

if __name__ == '__main__':
    encoded = Codec().encode(['123abc', 'xyz'])
    print(encoded)
    decoded = Codec().decode(encoded)
    print(decoded)