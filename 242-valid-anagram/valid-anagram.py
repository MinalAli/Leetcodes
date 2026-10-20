class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}

        for ch in s:
            if ch in d1:
                d1[ch] += 1
            else:
                d1[ch] = 1

        for ch in t:
            if ch in d2:
                d2[ch] += 1
            else:
                d2[ch] = 1
        

        # if d1.keys() != d2.keys():
        #     return False

        # for letter in d1.keys():
        #     if d1[letter] != d2[letter]:
        #         return False

        # return True

        if d1 == d2:
            return True
        else:
            return False
