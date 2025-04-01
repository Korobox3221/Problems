class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        lengths = len(s)
        lengtht = len(t)
        count = 0
        if lengtht != lengths:
            return  False
        for i in range(lengths):
            for x in t:
                if s[i] == x:
                    t.remove(x)
                    count += 1
                    break
        if count == lengths:
            return True
        else:
            return False