class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0

        char_set = set()

        count = 0
        res = 0

        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
                count += 1
                res = max(res, count)
            else:
                char_set.remove(s[l])
                l += 1
                count -= 1
                    



        return res
            
            
        