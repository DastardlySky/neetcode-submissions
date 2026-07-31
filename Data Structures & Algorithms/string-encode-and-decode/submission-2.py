class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))+"#"+word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        l = 0
        word_length = ""
        while l < len(s):
            if s[l] == "#":
                decoded.append(s[l+1:l+1+int(word_length)])
                l += int(word_length) + 1
                word_length = ""
            else:
                word_length += s[l]
                l += 1
        return decoded
            
