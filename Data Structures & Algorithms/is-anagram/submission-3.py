class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        t_d = {}
        for c in s:
            if c in s_d.keys():
                s_d[c] = s_d[c] + 1
            else:
                s_d[c] = 1
        for c in t:
            if c not in s_d:
                return False
            else:
                s_d[c] = s_d[c] - 1
                if s_d[c] < 0:
                    return False
        if any(s_d.values()) > 0:
            return False
        return True