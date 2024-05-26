class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        i = j = 0
        lenght = len(s)
        lenght, _max = (0,0) if not lenght else (lenght,0)
        while j<lenght:
            if s[j] not in res:
                res.add(s[j])
                if _max <= j-i:
                    _max = j-i+1
                j += 1
            else:
                res.remove(s[i])
                i += 1
        return _max
