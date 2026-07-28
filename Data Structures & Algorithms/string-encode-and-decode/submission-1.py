class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + " " + string
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        index = 0
        try:
            while True:
                string_len = ""
                while s[index] != " ":
                    string_len = string_len + s[index]
                    index += 1
                decoded.append(s[index + 1 : index + int(string_len) + 1])
                index += int(string_len) + 1
        finally:
            return decoded
