class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0

        chars = {}
        l, r = 0, 0

        chars[s[l]] = 1
        while r < len(s):

            max_count = 0
            max_char = ""
            for char, count in chars.items():
                if count > max_count:
                    max_count = count
                    max_char = char
            
            print(max_count, max_char, s[l:r+1])

            if (r - l + 1) - max_count <= k:
                res = max(res, (r - l + 1))
                r += 1
                if r == len(s):
                    continue
                if s[r] in chars:
                    chars[s[r]] += 1
                else:
                    chars[s[r]] = 1
            else:
                chars[s[l]] -= 1
                l += 1
            
        return res

            


        
        