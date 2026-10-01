class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] != "#":
                j += 1

            l = int(s[i:j])
            i = j + l + 1
            word = s[j + 1: i]
            decoded.append(word)

        return decoded