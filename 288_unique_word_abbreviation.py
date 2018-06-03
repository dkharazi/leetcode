# 288 Unique Word Abbreviation

# An abbreviation of a word follows the form <first letter><number><last letter>. 
# Below are some examples of word abbreviations:

# a) it                      --> it    (no abbreviation)

#      1
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n

# Assume you have a dictionary and given a word, 
# find whether its abbreviation is unique in the dictionary. 
# A word’s abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Example:

# Given dictionary = [ "deer", "door", "cake", "card" ]

# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]

        build a dictionary in which key is first letter and last letter plus the length between them. 
        Then a word (transformed into first letter+length+last letter) is unique if:
        1. the dictionary doesn’t have the word as key at all
        2. the dictionary has the word as key. 
        But the value corresponding to the key is a set only containing the word. 
        That means, the current word is the only word with same transformation in dictionary.
        """
        self.func = lambda s: s[0] + str(len(s)-2) + s[-1]
        ab = ((self.func(word), word) for word in dictionary)
        d = {}
        for k, v in ab:
            if not d.get(k):
                d[k] = set()
            d[k].add(v)
        self.d = d

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        key = self.func(word)
        if not self.d.get(key):
            return True
        else:
            if word in self.d[key] and len(self.d[key]) == 1:
                return True
        return False

if __name__ == '__main__':
    # Your ValidWordAbbr object will be instantiated and called as such:
    # vwa = ValidWordAbbr(dictionary)
    # vwa.isUnique("word")
    # vwa.isUnique("anotherWord")
    dictionary = [ "deer", "door", "cake", "card" ]
    vwa = ValidWordAbbr(dictionary)
    print(vwa.isUnique('dear'))
    print(vwa.isUnique('cart'))
    print(vwa.isUnique('cane'))
    print(vwa.isUnique('make'))